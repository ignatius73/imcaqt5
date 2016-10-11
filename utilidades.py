import sys, re
from PyQt5 import QtCore, QtGui, QtSql, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget


class Utilidades():

    def __init__(self):
        super(Utilidades, self).__init__()

    def validar_vacios(self, i):
        #  Valido si el campo está vacío
        if i.text() == "":
            i.setStyleSheet("background-color: cyan")
            p = QtCore.QPoint()
            p.setX = 50
            p.setY = 82
            QtWidgets.QToolTip.showText(p, "No puede estar vacío", i)
            return False
        else:
            return True

    def Confirmar(self, t):
        '''Muestra Cuadro de dialogo para la confirmacion. Recibe el texto a mostrar'''
        '''Creo el Cuadro de dialogo'''
        w = QtWidgets.QWidget()
        v = QMessageBox.question(w, "Atención", t, QMessageBox.Ok | QMessageBox.Cancel)
        w.show()
        return v

##############################################################################

    def Convierto_a_Lista(self, obj):
        '''Recibe un QtSqlQuery y devuelve una Lista'''
        if isinstance(obj, QtSql.QSqlQuery):
            l = []
            while obj.next():
                l.append(obj.record())
            return l
        else:
            return "No me diste un Query"

##############################################################################

    def Convierto_a_tabla(self, obj):
        '''Recibe un QtSqlQuery y devuelve una Lista de listas'''
        if isinstance(obj, QtSql.QSqlQuery):
            l = []
            a = []

            while obj.next():
                l.append(obj.record())
            for i in l:
                b = []
                for r in range(i.count()):
                    b.append(i.value(r))
                a.append(b)
                b = None

            return a
        else:
            return "No me diste un Query"

##############################################################################

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

##############################################################################

    def Pruebo_Tipo(self, v):
        try:
            v = float(v)
            return v
        except:
            return False

#################################################################

    def Mensaje(self, msg):
        ventana = QtWidgets.QMessageBox()
        ventana.setText(msg)
        ventana.setIcon(QMessageBox.Information)
        ventana.setStandardButtons(QMessageBox.Ok)
        return ventana

#################################################################

    def CreoTabla(self, q, campos):
        '''Recibe una query'''
#        self.setWindowTitle("Módulo de Calificaciones")
#        self.frm = QtWidgets.QFrame()
#        self.layout = QtWidgets.QGridLayout()
#        self.setLayout(self.layout)
#        self.sb = QtWidgets.QScrollArea()
#        self.et = QtWidgets.QLabel()
        self.table = QtWidgets.QTableWidget()
#        self.sb.setWidget(self.frm)
#        self.layout.addWidget(self.table)
        self.table.setColumnCount(len(campos))
        self.table.setHorizontalHeaderLabels(campos)
        row = 0
        col = 0
        while q.next():
            self.table.insertRow(row)
            for i in campos:
                self.table.setItem(row, col, QtWidgets.QTableWidgetItem(str(q.value(col))))
                self.table.resizeColumnToContents(col)
                col = col + 1
            self.table.resizeRowToContents(row)

            row = row + 1
            col = 0

        '''Divido el ancho por la cantidad de filas'''

        return self.table
