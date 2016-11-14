import sys, datetime
#  import pymysql

from PyQt5 import QtCore, QtGui, uic, QtSql, QtWidgets
from asignaturas import *
from conn import *
from PyQt5.QtCore import QDate, QVariant
from utilidades import *
from modificaciones import *
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QPixmap
from recibo import *


class Caja(QtWidgets.QWidget):

    def __init__(self, usr):
        super(Caja, self).__init__()
        self.usr = usr
        self.conn = Connection()
        self.db = self.conn.conecto_a_DB(self.usr, 'Cooperadora')

##############################################################################

    def formularioCaja(self):
        '''Cargo el archivo ui'''
        util = Utilidades()
        self.ui = uic.loadUi("cooperadora.ui", self)
        self.model = QtSql.QSqlTableModel(None, self.db)
        self.layIzq = QtWidgets.QVBoxLayout()
        self.layIzq.setSpacing(5)
        self.layDer = QtWidgets.QHBoxLayout()
        self.layout = QtWidgets.QGridLayout()
        self.botonera = QtWidgets.QHBoxLayout()
        entero = QtGui.QDoubleValidator()
        self.importe = QtWidgets.QLineEdit()
        self.importe.setValidator(entero)
        self.concepto = QtWidgets.QLineEdit()

        tipos = ["Tipo A", "Tipo B"]
        self.tipo = QtWidgets.QComboBox()
        self.tipo.addItems(tipos)

        self.t = QtWidgets.QTableWidget()
        p = QtGui.QPixmap()
        p.load('imagenes/cacharros.jpg')
        img = QtWidgets.QLabel()
        img.setPixmap(p)
        img.setScaledContents(True)
        h = img.height()
        w = img.width()
        img.setPixmap(p.scaled(w, h, 1))
        img.setScaledContents(True)
        head = QtWidgets.QHeaderView(Qt.Horizontal)
        head.setSectionResizeMode(1)
        self.t.setHorizontalHeader(head)
        self.t.setColumnCount(5)
        self.t.setHorizontalHeaderLabels(['Importe', 'Saldo', 'Detalle', 'Recibo'])
        self.agregar = QtWidgets.QPushButton("Agregar")
        self.CleanBtn = QtWidgets.QPushButton("Limpiar")
        self.recibo = QtWidgets.QPushButton("Recibo")
        self.botonera.addWidget(self.agregar)
        self.botonera.addWidget(self.recibo)
        self.botonera.addWidget(self.CleanBtn)
        self.x = QtWidgets.QLineEdit()
        self.model.setTable('caja')
        self.model.setSort(0, 1)
        self.model.select()
        self.head = QtWidgets.QHeaderView(Qt.Horizontal)
        self.head.setSectionResizeMode(1)
        self.caja = QtWidgets.QTableView()
        self.caja.setModel(self.model)
        self.caja.setHorizontalHeader(self.head)
        self.caja.setSelectionMode(3)
        self.caja.hideColumn(0)
        util.estiloTablas(self.model, self.caja)
        self.caja.show()
        self.lbl = QtWidgets.QLabel("Importe")
        self.lbl2 = QtWidgets.QLabel("Detalle")
        self.lbl3 = QtWidgets.QLabel("Tipo de Movimiento")
        self.layIzq.addWidget(self.lbl)
        self.layIzq.addWidget(self.importe)
        self.layIzq.addWidget(self.lbl2)
        self.layIzq.addWidget(self.concepto)
        self.layIzq.addWidget(self.lbl3)
        self.layIzq.addWidget(self.tipo)
        self.layIzq.addItem(self.botonera)
        self.layIzq.addWidget(self.caja)
#        self.layDer.addStretch()
        self.layDer.addWidget(img)
        self.layout.addItem(self.layIzq, 0, 0)
        self.layout.addItem(self.layDer, 0, 1)
        self.ui.setLayout(self.layout)
        self.agregar.clicked.connect(self.agrega)
#        self.caja.clicked.connect(self.agrega)
        self.CleanBtn.clicked.connect(self.limpia)
        self.recibo.clicked.connect(self.doRecibo)



##############################################################################

    def agrega(self, x):
        '''Agrega importe'''
        importe = float(self.importe.text())
        concepto = self.concepto.text()
        tipo = self.tipo.currentIndex()
        saldo = self.saldo()
        saldo = saldo + importe
        sql = "INSERT INTO caja (Importe, detalle, Saldo, tipo, fecha) VALUES (:imp, :det,"\
        " :saldo, :tipo, CURDATE())"
        q = QtSql.QSqlQuery(self.db.database('Cooperadora'))
        q.prepare(sql)
        q.bindValue(":imp", importe)
        q.bindValue(":det", concepto)
        q.bindValue(':saldo', saldo)
        q.bindValue(":tipo", tipo)
        util = Utilidades()
        util.ejecuto(q, 'Cooperadora')

#        self.model.setSort(2, 1)
        self.model.select()

##############################################################################

    def quita(self, x):
        self.t.removeRow(x.row())

##############################################################################

    def saldo(self):
        '''Devuelve el saldo de caja'''
        util = Utilidades()
        sql = "SELECT saldo FROM caja ORDER BY idMovimiento DESC LIMIT 1"
        q = QtSql.QSqlQuery(self.db.database('Cooperadora'))
        q.prepare(sql)
        ej = util.ejecuto(q, 'Cooperadora')
        saldo = 0
        if ej.size() > 0:
            while ej.next():
                saldo = ej.value(0)
        return saldo

##############################################################################

    def limpia(self):
        util = Utilidades()

        for i in self.findChildren(QtWidgets.QLineEdit):
            util.limpia(i)

##############################################################################

    def doRecibo(self):
        recibo = Recibo()
        datos = ['Gabriel García', 1]
        recibo.creaRecibo(datos)
