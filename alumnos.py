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


class Alumnos(QtWidgets.QWidget):

    def __init__(self, usr):
        super(Alumnos, self).__init__()
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

        '''QLineEdit Filtrar'''
        self.lnFiltrar = QtWidgets.QLineEdit()

        '''Combo Actividades'''
        tipos = ["", "Modificar Alumno", "Agregar Calificaciones", "Borrar Alumno", "Inscribir Asignaturas"]
        self.tipo = QtWidgets.QComboBox()
        self.tipo.addItems(tipos)


        self.layout = QtWidgets.QGridLayout()
#        self.botonera = QtWidgets.QHBoxLayout()
#        entero = QtGui.QDoubleValidator()
        self.filtra = QtWidgets.QPushButton("Filtrar")
        self.CleanBtn = QtWidgets.QPushButton("Limpiar")
        self.recibo = QtWidgets.QPushButton("Recibo")

        self.model.setTable('alumnos')
        self.model.setSort(0, 1)
        self.model.select()
        self.head = QtWidgets.QHeaderView(Qt.Horizontal)
        self.head.setSectionResizeMode(1)
        self.caja = QtWidgets.QTableView()
        self.caja.setModel(self.model)
        self.caja.setHorizontalHeader(self.head)
        self.caja.setSelectionMode(3)
        self.caja.hideColumn(0)
        for i in range(3,47):
            if i != 15 and i != 29:
                self.caja.hideColumn(i)

        self.util.estiloTablas(self.model, self.caja)
        self.caja.show()

        '''Labels'''
        self.lbl = QtWidgets.QLabel("Nombre del Alumno")
        self.lbl3 = QtWidgets.QLabel("Tipo de Actividad")



#        self.top.addStretch()
        self.top.addWidget(self.lbl)
        self.top.addWidget(self.lnFiltrar)
        self.top.addWidget(self.lbl3)
        self.top.addWidget(self.tipo)


        self.top.setSpacing(8)
        self.top.addWidget(self.caja)


        self.layout.addItem(self.top, 0, 0)
        self.ui.setLayout(self.layout)
        self.filtra.clicked.connect(self.filtrar)
        self.CleanBtn.clicked.connect(self.limpia)
        self.recibo.clicked.connect(self.doRecibo)
        self.lnFiltrar.textChanged.connect(self.autocomp)
        self.caja.clicked.connect(self.filtrar)



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

    def filtrar(self, x):
        r = x.row()
        a = self.model.record(r)

        talumno = [a.value(1), a.value(2),self.tipo.currentText()]

        pa = self.parentWidget()
        pa.control(talumno)

##############################################################################

    def autocomp(self):
        txt = ''
        txt = txt + 'Nombre LIKE "%' + self.lnFiltrar.text() + '%"'
        self.model.setFilter(txt)
        self.model.select()

##############################################################################

    def borrar_Alumno(self, dni):

        util = Utilidades()

        oka = util.MensajeOkNo("¿Estás segurx de borrar al alumno? Esta operación no puede deshacerse")

        res = oka.exec_()

        if res == 1024:

            sql = "DELETE FROM alumnos WHERE DNI = :dni"

            q = QtSql.QSqlQuery(self.db.database('Cooperadora'))

            q.prepare(sql)

            q.bindValue(":dni", dni)

            ej = util.ejecuto(q, 'Cooperadora')