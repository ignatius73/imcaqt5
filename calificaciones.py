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
        self.resize(800, 600)
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)
        self.table = QtWidgets.QTableWidget()
        self.layout.addWidget(self.table)
        self.table.itemChanged.connect(self.Actualizar_Nota)

        sql = "SELECT calificaciones.*, alumnos.Nombre as alum, " \
        "asignaturas.nombre as asig from calificaciones " \
        "INNER JOIN alumnos on alumnos.DNI= calificaciones.alumno " \
        "INNER JOIN asignaturas " \
        "on asignaturas.id_asignatura = calificaciones.id_asign " \
        "WHERE alumnos.DNI = :dni"

        self.table.setColumnCount(12)
        self.table.setHorizontalHeaderLabels(['Nombre', 'Asignatura', '1er Parcial', '2do Parcial', 'Recuperatorio', 'Final 1', 'Final 2', 'Final 3', 'Final 4', 'Nota Final', 'Fecha Final', 'ID'])
        q= QtSql.QSqlQuery(self.db.database("calificaciones"))
        q.prepare(sql)
        q.bindValue(":dni", self.dni)
        ej = Utilidades()
        estado = ej.ejecuto(q, 'calificaciones')
        print(estado.size())
        row = 0
        while estado.next():
            self.table.insertRow(row)
            id = QtWidgets.QTableWidgetItem(str(estado.value(0)))
            nombre = QtWidgets.QTableWidgetItem(str(estado.value(12)))
            asig = QtWidgets.QTableWidgetItem(str(estado.value(13)))
            p1 = QtWidgets.QTableWidgetItem(str(estado.value(2)))
            p2 = QtWidgets.QTableWidgetItem(str(estado.value(3)))
            re = QtWidgets.QTableWidgetItem(str(estado.value(4)))
            fi1 = QtWidgets.QTableWidgetItem(str(estado.value(5)))
            fi2 = QtWidgets.QTableWidgetItem(str(estado.value(6)))
            fi3 = QtWidgets.QTableWidgetItem(str(estado.value(7)))
            fi4 = QtWidgets.QTableWidgetItem(str(estado.value(8)))
            nota = QtWidgets.QTableWidgetItem(str(estado.value(9)))
            fecha = QtWidgets.QTableWidgetItem(str(estado.value(10)))
            self.table.setItem(row, 0, nombre)
            self.table.setItem(row, 1, asig)
            self.table.setItem(row, 2, p1)
            self.table.setItem(row, 3, p2)
            self.table.setItem(row, 4, re)
            self.table.setItem(row, 5, fi1)
            self.table.setItem(row, 6, fi2)
            self.table.setItem(row, 7, fi3)
            self.table.setItem(row, 8, fi4)
            self.table.setItem(row, 9, nota)
            self.table.setItem(row, 10, fecha)
            self.table.setItem(row,11, id)
            row = row + 1

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
        ide = self.table.item(row, 12)
        print("ID " + str(id))
        value = self.table.currentItem()
        columns = ['Nombre', 'Asignatura', '1er Parcial', '2do Parcial', 'Recuperatorio', 'Final 1', 'Final 2', 'Final 3', 'Final 4', 'Nota Final', 'Fecha Final', 'id']
        sql = "UPDATE calificaciones SET " + columns[column] + "= :value WHERE id = :id"
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