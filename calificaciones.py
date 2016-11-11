import sys
from PyQt5 import QtCore, QtSql, uic, QtWidgets, QtPrintSupport
from conn import *
from utilidades import *
from asignaturas import *
from PyQt5.QtCore import QDate
from PyQt5.QtCore import Qt

class Calificaciones(QtWidgets.QWidget):

    def __init__(self, usr):
        super(Calificaciones, self).__init__()
        self.usr = usr
        self.Conecto_a_DB()


##############################################################################

    def Listado(self, dni):
        '''Obtengo todas las materias anotadas del usuario'''
        self.dni = dni

        # Doy nombre a la ventana
        self.setWindowTitle("Módulo de Calificaciones")
        self.frm = QtWidgets.QFrame()
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)
        self.sb = QtWidgets.QScrollArea()
        self.et = QtWidgets.QLabel()
        self.et.setText("Nombre del Alumno")
        self.nombre = QtWidgets.QLineEdit()
        self.print = QtWidgets.QPushButton("Guardar")

        self.table = QtWidgets.QTableWidget()
        self.sb.setWidget(self.frm)
        self.layout.addWidget(self.et)
        self.layout.addWidget(self.nombre)
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.print)


        sql = "SELECT calificaciones.*, alumnos.Nombre as alum, " \
        "asignaturas.nombre as asig from calificaciones " \
        "INNER JOIN alumnos on alumnos.DNI= calificaciones.alumno " \
        "INNER JOIN asignaturas " \
        "on asignaturas.id_asignatura = calificaciones.id_asign " \
        "WHERE alumnos.DNI = :dni"

        self.head = QtWidgets.QHeaderView(Qt.Horizontal)
        self.head.setSectionResizeMode(1)
        self.table.setHorizontalHeader(self.head)

        self.table.setColumnCount(10)
        self.table.setHorizontalHeaderLabels(['Asignatura', '1er Parcial', '2do Parcial', 'Recuperatorio', 'Final 1', 'Final 2', 'Final 3', 'Final 4', 'Nota Final', 'ID'])
        q= QtSql.QSqlQuery(self.db.database("calificaciones"))
        q.prepare(sql)
        q.bindValue(":dni", self.dni)
        self.ej = Utilidades()
        estado = self.ej.ejecuto(q, 'calificaciones')


        row = 0


        while estado.next():

            self.nombre.setText(estado.value(13))
            self.table.insertRow(row)
            ide = QtWidgets.QTableWidgetItem(str(estado.value(0)))
            ide.setFlags(QtCore.Qt.ItemIsEnabled)

            asig = QtWidgets.QTableWidgetItem(str(estado.value(14)))
            asig.setFlags(QtCore.Qt.ItemIsEnabled)
            p1 = QtWidgets.QTableWidgetItem(str(estado.value(2)))
            p2 = QtWidgets.QTableWidgetItem(str(estado.value(3)))
            re = QtWidgets.QTableWidgetItem(str(estado.value(4)))
            fi1 = QtWidgets.QTableWidgetItem(str(estado.value(5)))
            fi2 = QtWidgets.QTableWidgetItem(str(estado.value(6)))
            fi3 = QtWidgets.QTableWidgetItem(str(estado.value(7)))
            fi4 = QtWidgets.QTableWidgetItem(str(estado.value(8)))
            nota = QtWidgets.QTableWidgetItem(str(estado.value(9)))
            self.table.setItem(row, 0, asig)
            self.table.setItem(row, 1, p1)
            self.table.setItem(row, 2, p2)
            self.table.setItem(row, 3, re)
            self.table.setItem(row, 4, fi1)
            self.table.setItem(row, 5, fi2)
            self.table.setItem(row, 6, fi3)
            self.table.setItem(row, 7, fi4)
            self.table.setItem(row, 8, nota)
            self.table.setItem(row,9, ide)
            row = row + 1

        self.table.itemChanged.connect(self.Actualizar_Nota)
        self.print.clicked.connect(self.Imprimir)
#        self.nombre.textChanged.connect(self.autocomp)  #future
##############################################################################

    def Conecto_a_DB(self):
        try:
            self.db
        except:
            conn = Connection()
            conn.SetUsuario(self.usr)
            self.db = conn.CreateConnection('calificaciones')
            if self.db.database('calificaciones').isOpen():
                print("Conexión exitosa a Calificaciones")

##############################################################################

    def Actualizar_Nota(self):
        column = self.table.currentColumn()
        row = self.table.currentRow()
        ide = self.table.item(row, 9).text()
        max = self.table.columnCount()

        v = self.table.currentItem().text()
        value = self.ej.Pruebo_Tipo(v)
        if value is False:
            msg = self.ej.Mensaje("Debe ser un número")
            msg.exec_()
        else:
            ide = int(ide)
            columns = ['Asignatura', '1er Parcial', '2do Parcial', 'Recuperatorio', 'Final 1', 'Final 2', 'Final 3', 'Final 4', 'Nota Final', 'id']
            columnas = ['asig','cuatri1', 'cuatri2', 'recup', 'final1', 'final2', 'final3', 'final4', 'nota', 'fecha_final']
            sql = "UPDATE calificaciones SET " + columnas[column] + "= :value WHERE id_calif = :id"
            q = QtSql.QSqlQuery(self.db.database('calificaciones'))
            q.prepare(sql)
            q.bindValue(":value", value)
            q.bindValue(":id", ide)
            self.ejecuto(q, 'calificaciones')
            self.cohorte()

################################################################

    def ejecuto(self, q, db):
        estado = q.exec_()
        pipi = q.executedQuery()
        if estado is True:

            if q.isActive() is False:
                print("La consulta no está activa")
            else:
                return q
        else:
            print(pipi)
            print((self.db.database(db).lastError()))

##############################################################################

    def Imprimir(self):
        x = self.parentWidget()
        x.alumnos()

##############################################################################

    def cohorte(self):

        '''Controlo que el DNI no tenga cohorte en la tabla de alumnos'''
        sql = "SELECT COUNT(*) FROM alumnos WHERE alumnos.DNI = :dni AND alumnos.cohorte IS NULL"
        q = QtSql.QSqlQuery(self.db.database('calificaciones'))
        q.prepare(sql)
        q.bindValue(":dni", self.dni)
        estado = self.ejecuto(q,'calificaciones')
        while estado.next():
            if estado.value(0) == 1:
                sql = "SELECT COUNT(*) FROM calificaciones " \
                "INNER JOIN asignaturas on calificaciones.id_asign = "\
                "asignaturas.id_asignatura WHERE calificaciones.alumno = "\
                ":dni AND asignaturas.anio = 0 AND calificaciones.nota >= 4"
                q = QtSql.QSqlQuery(self.db.database('calificaciones'))
                q.prepare(sql)
                q.bindValue(":dni", self.dni)
                estado = self.ejecuto(q, 'calificaciones')
                anio = QDate.currentDate()
                while estado.next():
                    if estado.value(0) == 8:
                        sql = "UPDATE alumnos SET cohorte = :anio WHERE DNI = :dni"
                        q = QtSql.QSqlQuery(self.db.database('calificaciones'))
                        q.prepare(sql)
                        q.bindValue(":anio", anio.year())
                        q.bindValue(":dni", self.dni)
                        estado = self.ejecuto(q,'calificaciones')
