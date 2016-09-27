import sys
from PyQt5 import QtCore, QtSql, uic, QtWidgets
from conn import *
from utilidades import *
from asignaturas import *

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

        self.table = QtWidgets.QTableWidget()
        self.sb.setWidget(self.frm)
        self.layout.addWidget(self.et)
        self.layout.addWidget(self.nombre)
        self.layout.addWidget(self.table)


        sql = "SELECT calificaciones.*, alumnos.Nombre as alum, " \
        "asignaturas.nombre as asig from calificaciones " \
        "INNER JOIN alumnos on alumnos.DNI= calificaciones.alumno " \
        "INNER JOIN asignaturas " \
        "on asignaturas.id_asignatura = calificaciones.id_asign " \
        "WHERE alumnos.DNI = :dni"

        self.table.setColumnCount(10)
        self.table.setHorizontalHeaderLabels(['Asignatura', '1er Parcial', '2do Parcial', 'Recuperatorio', 'Final 1', 'Final 2', 'Final 3', 'Final 4', 'Nota Final', 'ID'])
        q= QtSql.QSqlQuery(self.db.database("calificaciones"))
        q.prepare(sql)
        q.bindValue(":dni", self.dni)
        self.ej = Utilidades()
        estado = self.ej.ejecuto(q, 'calificaciones')


        row = 0


        while estado.next():
            self.nombre.setText(estado.value(12))
            self.table.insertRow(row)
            ide = QtWidgets.QTableWidgetItem(str(estado.value(0)))
            ide.setFlags(QtCore.Qt.ItemIsEnabled)

            asig = QtWidgets.QTableWidgetItem(str(estado.value(13)))
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

################################################################

    def ejecuto(self, q, db):
        estado = q.exec_()
        pipi = q.executedQuery()
        if estado is True:
            print("estado true")
            if q.isActive() is False:
                print("La consulta no está activa")
            else:
                return q
        else:
            print(pipi)
            print((self.db.database(db).lastError()))
