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
        self.periodo = QtWidgets.QLineEdit()
        self.estado = QtWidgets.QLineEdit()
        self.t = QtWidgets.QTableWidget()
        head = QtWidgets.QHeaderView(Qt.Horizontal)
        head.setSectionResizeMode(1)
        self.t.setHorizontalHeader(head)
        self.t.setColumnCount(5)
        self.t.setHorizontalHeaderLabels(['ID','Período', 'Importe', 'Detalle', 'DNI'])
        self.filtrar = QtWidgets.QPushButton("Filtrar")
        self.OkBtn = QtWidgets.QPushButton("Cobrar")
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
        self.lbl3 = QtWidgets.QLabel("Período")
        self.lbl4 = QtWidgets.QLabel("Estado")
        self.layIzq.addWidget(self.lbl)
        self.layIzq.addWidget(self.dni)
        self.layIzq.addWidget(self.lbl2)
        self.layIzq.addWidget(self.concepto)
        self.layIzq.addWidget(self.lbl3)
        self.layIzq.addWidget(self.periodo)
        self.layIzq.addWidget(self.lbl4)
        self.layIzq.addWidget(self.estado)

        self.layIzq.addItem(self.botonera)
        self.layIzq.addWidget(self.t)
#        self.layIzq.addStretch(2)

        self.layout.addItem(self.layIzq, 0, 0)
        self.layout.addItem(self.layDer, 0, 1)
        self.ui.setLayout(self.layout)
        self.filtrar.clicked.connect(self.filtro)
        self.OkBtn.clicked.connect(self.cobra)
        self.caja.clicked.connect(self.agrega)
        self.t.clicked.connect(self.quita)


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
        if self.periodo.text() != '':
            if txt != '':
                txt = txt + ' AND '
            txt = txt + 'periodo LIKE "' + self.periodo.text() + '"'
        if self.estado.text() != '':
            if txt != '':
                txt = txt + ' AND '
            txt = txt + 'estado LIKE "' + self.estado.text() + '"'
        self.model.setFilter(txt)
        self.model.select()

##############################################################################

    def agrega(self, x):

        row = x.row()

        a = self.model.record(row)

        print(a.value(0))
        if self.chequeo(a) is False:
            columns = a.count()
            print(columns)
            row = self.t.rowCount()
            print(row)
            self.t.insertRow(row)
            self.t.setItem(row, 0, QtWidgets.QTableWidgetItem(str(a.value(0))))
            self.t.setItem(row, 1, QtWidgets.QTableWidgetItem(a.value(1)))
            self.t.setItem(row, 2, QtWidgets.QTableWidgetItem(str(a.value(3))))
            self.t.setItem(row, 3, QtWidgets.QTableWidgetItem(a.value(4)))
            self.t.setItem(row, 4, QtWidgets.QTableWidgetItem(str(a.value(5))))
            self.t.setItem(row, 5, QtWidgets.QTableWidgetItem(a.value(5)))
            self.t.setItem(row, 5, QtWidgets.QTableWidgetItem(a.value(6)))

##############################################################################

    def quita(self, x):
        self.t.removeRow(x.row())

##############################################################################

    def cobra(self):
        if self.t.rowCount() > 0:
            self.recibos()
            sql = "INSERT INTO caja (Importe, Detalle) VALUES (:imp, :det)"
            rows = self.t.rowCount()
            for i in range(0, rows):
                id = int(self.t.item(i, 0).text())


##############################################################################

    def recibos(self):
        rows = self.t.rowCount()
        importe = 0
        detalle = ''
        dni = int(self.t.item(0,4).text())
        sql = "SELECT Nombre from alumnos WHERE DNI = :dni"
        q = QtSql.QSqlQuery(self.db.database('Cooperadora'))
        q.prepare(sql)
        q.bindValue(":dni", dni)
        util = Utilidades()
        ej = util.ejecuto(q,'cooperadora')
        while ej.next():
            nombre = ej.value(0)
        print (dni)
        print(nombre)
        for i in range(0, rows):
            pass

##############################################################################

    def chequeo(self, a):

        rows = self.t.rowCount()
        existe = False
        for i in range(0, rows):
            print("valor 0 de a" + str(a.value(0)))
            print(self.t.item(i, 0).text())
            if str(a.value(0)) == self.t.item(i,0).text():
                existe = True
        return existe