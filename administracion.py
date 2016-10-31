import sys, datetime
#  import pymysql

from PyQt5 import QtCore, QtGui, uic, QtSql, QtWidgets
from asignaturas import *
from conn import *
from PyQt5.QtCore import QDate, QVariant
from utilidades import *
from modificaciones import *
from PyQt5.QtCore import Qt, QSortFilterProxyModel

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
        self.layDer = QtWidgets.QHBoxLayout()
        self.layout = QtWidgets.QGridLayout()
        self.botonera = QtWidgets.QHBoxLayout()
        entero = QtGui.QIntValidator()
        self.dni = QtWidgets.QLineEdit()
        self.dni.setValidator(entero)
        self.concepto = QtWidgets.QLineEdit()
        self.importe = QtWidgets.QLineEdit()
        self.t = QtWidgets.QTableWidget()
        self.filtrar = QtWidgets.QPushButton("Filtrar")
        self.OkBtn = QtWidgets.QPushButton("Ingresar")
        self.CleanBtn = QtWidgets.QPushButton("Limpiar")
        self.recibo = QtWidgets.QPushButton("Recibo")
        self.botonera.addWidget(self.filtrar)
        self.botonera.addWidget(self.OkBtn)
        self.botonera.addWidget(self.recibo)
        self.botonera.addWidget(self.CleanBtn)

#        double = QtGui.QDoubleValidator()
#        self.importe.setValidator(double)
        self.x = QtWidgets.QLineEdit()
        self.model.setTable('cuentas')
        self.model.select()
        self.head = QtWidgets.QHeaderView(Qt.Horizontal)
        self.head.setSectionResizeMode(1)
        '''self.model.setHeaderData(3, Qt.Horizontal, '')
        self.model.setHeaderData(2, Qt.Horizontal, '')
        self.model.setHeaderData(2, Qt.Horizontal, '')'''
        self.caja = QtWidgets.QTableView()
        self.caja.setModel(self.model)

        self.caja.setHorizontalHeader(self.head)
        self.caja.setSelectionMode(3)
        self.caja.hideColumn(0)
        self.caja.hideColumn(2)
        self.caja.hideColumn(2)
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
        self.layIzq.addWidget(self.tabla_a_pagar)
        self.layIzq.addStretch(2)

        self.layout.addItem(self.layIzq, 0, 0)
        self.layout.addItem(self.layDer, 0, 1)
        self.ui.setLayout(self.layout)
        self.filtrar.clicked.connect(self.filtro)


        self.caja.clicked.connect(self.agrega)


##############################################################################

    def filtro(self):
        txt = ''
        if self.dni.text() != '':
            dni = self.dni.text()
            txt = txt + 'dni = ' + dni
        if self.concepto.text() != '':
            if txt != '':
                txt = txt + ' AND '
            txt = txt + 'detalle LIKE "' + self.concepto.text() + '"'
            print (self.concepto.text())
            print(txt)
        if self.importe.text() != '':
            if txt != '':
                txt = txt + ' AND '
            print (self.importe.text())
            print(txt)
            txt = txt + 'periodo LIKE "' + self.importe.text() + '"'
        self.model.setFilter(txt)
        self.model.select()

##############################################################################

    def agrega(self, x):
        print(type(x))
        row = x.row()
        a = self.model.record(row)
        print(type(a))
        print(a.value(0))
#        self.tabla_a_pagar.insertRow()
        rows = self.t.rowCount()
        col = self.t.columnCount()
        self.t.insertRow(rows + 1)
        self.t.insertColumn(col + 1)
