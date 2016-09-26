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
            QtGui.QToolTip.showText(p, "No puede estar vacío", i)
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