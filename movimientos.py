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


class Movimientos(QtWidgets.QWidget):

    def __init__(self, usr):
        super(Movimientos, self).__init__()
        self.usr = usr
        self.conn = Connection()
        self.db = self.conn.conecto_a_DB(self.usr, 'Cooperadora')

##############################################################################

    def formularioCaja(self):
        '''Cargo el archivo ui'''
        self.ui = uic.loadUi("cooperadora.ui", self)
        self.model = QtSql.QSqlTableModel(None, self.db)


        self.top = QtWidgets.QVBoxLayout()


        self.util = Utilidades()

        '''Combo Mes'''
        self.month = self.util.meses()
        self.meses = self.util.dicciolista(self.month)
        self.mes = QtWidgets.QComboBox()
        self.mes.addItems(self.meses)

        '''QDateEdit Año'''
        self.anio = QtWidgets.QDateEdit()
        anio = QtCore.QDate().currentDate()
        self.anio.setDisplayFormat('yyyy')
        self.anio.setDate(anio)

        '''Combo Tipo Listado'''
        tipos = ["Tipo A", "Tipo B"]
        self.tipo = QtWidgets.QComboBox()
        self.tipo.addItems(tipos)

        '''Combo Tipo de Movimiento'''
        mov = ["Ingresos", "Egresos"]
        self.mov = QtWidgets.QComboBox()
        self.mov.addItems(mov)

        self.layout = QtWidgets.QGridLayout()
        self.botonera = QtWidgets.QHBoxLayout()
#        entero = QtGui.QDoubleValidator()
        '''        self.importe = QtWidgets.QLineEdit()
        self.importe.setValidator(entero)
        self.concepto = QtWidgets.QLineEdit()
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
        self.t.setHorizontalHeaderLabels(['Importe', 'Saldo', 'Detalle', 'Recibo'])'''
        self.filtra = QtWidgets.QPushButton("Filtrar")
        self.CleanBtn = QtWidgets.QPushButton("Limpiar")
        self.recibo = QtWidgets.QPushButton("Recibo")
        self.botonera.addWidget(self.filtra)
        self.botonera.addWidget(self.recibo)
        self.botonera.addWidget(self.CleanBtn)
#        self.x = QtWidgets.QLineEdit()

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
        self.caja.show()

        '''Labels'''
        self.lbl = QtWidgets.QLabel("Mes")
        self.lbl2 = QtWidgets.QLabel("Año")
        self.lbl3 = QtWidgets.QLabel("Tipo de Listado")
        self.lbl4 = QtWidgets.QLabel("Tipo de Movimiento")

        '''Combos'''

#        self.top.addStretch()
        self.top.addWidget(self.lbl)
        self.top.addWidget(self.mes)
        self.top.addWidget(self.lbl2)
        self.top.addWidget(self.anio)
        self.top.addWidget(self.lbl3)
        self.top.addWidget(self.tipo)
        self.top.addWidget(self.lbl4)
        self.top.addWidget(self.mov)
        self.top.addItem(self.botonera)
        self.top.setSpacing(8)
        self.top.addWidget(self.caja)

#        self.layIzq.addItem(self.botonera)
#        self.layIzq.addWidget(self.caja)
#        self.layDer.addStretch()
#        self.layDer.addWidget(img)
#        self.layout.addItem(self.layIzq, 0, 0)
#        self.layout.addItem(self.layDer, 0, 1)
        self.layout.addItem(self.top, 0, 0)
        self.ui.setLayout(self.layout)
        self.filtra.clicked.connect(self.filtrar)
#        self.caja.clicked.connect(self.agrega)
        self.CleanBtn.clicked.connect(self.limpia)
        self.recibo.clicked.connect(self.doRecibo)



##############################################################################

    def agrega(self, x):
        '''Agrega importe'''
        importe = float(self.importe.text())
        concepto = self.concepto.text()
        saldo = self.saldo()
        saldo = saldo + importe
        sql = "INSERT INTO caja (Importe, detalle, Saldo) VALUES (:imp, :det,"\
        " :saldo)"
        q = QtSql.QSqlQuery(self.db.database('Cooperadora'))
        q.prepare(sql)
        q.bindValue(":imp", importe)
        q.bindValue(":det", concepto)
        q.bindValue(':saldo', saldo)
        util = Utilidades()
        util.ejecuto(q, 'Cooperadora')
        print(importe)
        print(concepto)
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

##############################################################################

    def filtrar(self):
        txt = ''
        mes = self.mes.currentText()
        mesnro = self.util.invDict(self.month)
        mesnum =  mesnro.get(mes)
        print(mesnum)
        txt = txt + 'MONTH(fecha) = ' + str(mesnum)
        print(txt)
        '''    dni = self.dni.text()
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
        '''
        self.model.setFilter(txt)
        self.model.select()


##############################################################################