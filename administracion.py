import sys, datetime
#  import pymysql

from PyQt5 import QtCore, QtGui, uic, QtSql, QtWidgets
from asignaturas import *
from conn import *
from PyQt5.QtCore import QDate, QVariant
from utilidades import *
from modificaciones import *
from PyQt5.QtCore import Qt

class Administracion(QtWidgets.QWidget):

    def __init__(self, usr):
        super(Administracion, self).__init__()
        self.usr = usr
        self.conn = Connection()
        self.db = self.conn.conecto_a_DB(self.usr, 'Cooperadora')

##############################################################################

    def formularioCoop(self):
        '''Cargo el archivo ui'''
        self.ui = uic.loadUi("cooperadora.ui", self)
        self.model = QtSql.QSqlTableModel(None, self.db)
        self.layIzq = QtWidgets.QVBoxLayout()
        self.layIzq.setSpacing(5)
        self.layDer = QtWidgets.QVBoxLayout()
        self.layout = QtWidgets.QGridLayout()
        self.botonera = QtWidgets.QHBoxLayout()
        entero = QtGui.QIntValidator()
        self.dni = QtWidgets.QLineEdit()
        self.dni.setValidator(entero)
        self.concepto = QtWidgets.QLineEdit()
        self.importe = QtWidgets.QLineEdit()
        self.OkBtn = QtWidgets.QPushButton("Ingresar")
        self.CleanBtn = QtWidgets.QPushButton("Limpiar")
        self.recibo = QtWidgets.QPushButton("Recibo")
        self.botonera.addWidget(self.OkBtn)
        self.botonera.addWidget(self.recibo)
        self.botonera.addWidget(self.CleanBtn)
        double = QtGui.QDoubleValidator()
        self.importe.setValidator(double)
        self.x = QtWidgets.QLineEdit()
        self.model.setTable('cooperadora')
        self.model.select()
        self.head = QtWidgets.QHeaderView(Qt.Horizontal)
        self.head.setSectionResizeMode(1)
        '''self.model.setHeaderData(3, Qt.Horizontal, '')
        self.model.setHeaderData(2, Qt.Horizontal, '')
        self.model.setHeaderData(2, Qt.Horizontal, '')'''
        self.caja = QtWidgets.QTableView()
        self.caja.setModel(self.model)
        self.caja.setHorizontalHeader(self.head)

        self.caja.hideColumn(0)
        self.caja.show()
        self.layDer.addWidget(self.caja)
        self.lbl = QtWidgets.QLabel("Ingresa Dni del Alumno")
        self.lbl2 = QtWidgets.QLabel("Detalle")
        self.lbl3 = QtWidgets.QLabel("Importe")
        self.layIzq.addWidget(self.lbl)
        self.layIzq.addWidget(self.dni)
        self.layIzq.addWidget(self.lbl2)
        self.layIzq.addWidget(self.concepto)
        self.layIzq.addWidget(self.lbl3)
        self.layIzq.addWidget(self.importe)

        self.layIzq.addItem(self.botonera)
        self.layIzq.addStretch(2)
        self.layout.addItem(self.layIzq, 0, 0)
        self.layout.addItem(self.layDer, 0, 1)
        self.ui.setLayout(self.layout)