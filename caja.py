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
        self.saldo1 = QtWidgets.QLineEdit()
        self.saldo1.setValidator(entero)
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
        self.lbl4 = QtWidgets.QLabel("Saldo de Caja")
        self.layIzq.addWidget(self.lbl)
        self.layIzq.addWidget(self.importe)
        self.layIzq.addWidget(self.lbl2)
        self.layIzq.addWidget(self.concepto)
        self.layIzq.addWidget(self.lbl3)
        self.layIzq.addWidget(self.tipo)
        self.layIzq.addItem(self.botonera)
        self.layIzq.addWidget(self.caja)
        self.layIzq.addWidget(self.lbl4)
        self.layIzq.addWidget(self.saldo1)
#        self.layDer.addStretch()
        self.layDer.addWidget(img)
        self.layout.addItem(self.layIzq, 0, 0)
        self.layout.addItem(self.layDer, 0, 1)
        s = self.saldo()
        self.saldo1.setText(str(s))
        self.ui.setLayout(self.layout)
        self.agregar.clicked.connect(self.agrega)
        self.caja.doubleClicked.connect(self.quita)
        self.CleanBtn.clicked.connect(self.limpia)
        self.recibo.clicked.connect(self.doRecibo)



##############################################################################

    def agrega(self, x):
        '''Agrega importe'''
        importe = float(self.importe.text())
        concepto = self.concepto.text()
        tipo = self.tipo.currentIndex()
        sql = "INSERT INTO caja (Importe, detalle, tipo, fecha) VALUES (:imp, :det,"\
        ":tipo, CURDATE())"
        q = QtSql.QSqlQuery(self.db.database('Cooperadora'))
        q.prepare(sql)
        q.bindValue(":imp", importe)
        q.bindValue(":det", concepto)
        q.bindValue(":tipo", tipo)
        util = Utilidades()
        util.ejecuto(q, 'Cooperadora')

#        self.model.setSort(2, 1)
        self.model.select()
        r = self.saldo()
        self.saldo1.setText(str(r))

##############################################################################

    def quita(self, x):
        v = Utilidades()
        r = v.MensajeOkNo("¿Estás segurx? Esta acción no puede deshacerse")
        t = r.exec_()
        if t == 1024:

            self.model.removeRow(x.row())
            self.model.submitAll()
            self.model.select()
            r = self.saldo()
            self.saldo1.setText(str(r))


##############################################################################

    def saldo(self):
        '''Devuelve el saldo de caja'''
        util = Utilidades()
        sql = "SELECT SUM(Importe) FROM caja"
        q = QtSql.QSqlQuery(self.db.database('Cooperadora'))
        q.prepare(sql)
        ej = util.ejecuto(q, 'Cooperadora')
        saldo = 0
        if ej.size() > 0:
            ej.first()
            saldo = ej.value(0)
        print(saldo)
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
