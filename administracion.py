import sys, datetime
#  import pymysql

from PyQt5 import QtCore, QtGui, uic, QtSql, QtWidgets
from asignaturas import *
from conn import *
from PyQt5.QtCore import QDate, QVariant
from utilidades import *
from modificaciones import *
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from recibo import *

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
#        self.model = QtSql.QSqlQueryModel()
        self.cuenta = 0
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
        self.nombre = QtWidgets.QLineEdit()
        self.t = QtWidgets.QTableWidget()
        self.total = QtWidgets.QLineEdit()
        head = QtWidgets.QHeaderView(Qt.Horizontal)
        head.setSectionResizeMode(1)
        self.t.setHorizontalHeader(head)
        self.t.setColumnCount(6)
        self.t.setHorizontalHeaderLabels(['ID','Alumno', 'Período', 'Importe', 'Detalle', 'DNI'])
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
        self.lbl5 = QtWidgets.QLabel("Total")
        self.lbl6 = QtWidgets.QLabel("Nombre del Alumno")
        self.layIzq.addWidget(self.lbl6)
        self.layIzq.addWidget(self.nombre)
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
        self.layIzq.addWidget(self.lbl5)
        self.layIzq.addWidget(self.total)
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
        if self.nombre.text() != '':
            print(self.nombre.text())
            if txt != '':
                txt = txt + ' AND '
            txt = txt + 'Alumno LIKE "%' + self.nombre.text() + '%"'
        if self.concepto.text() != '':
            if txt != '':
                txt = txt + ' AND '
            txt = txt + 'detalle LIKE "' + self.concepto.text() + '"'
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
        print(txt)
        self.model.setFilter(txt)
        self.model.select()

##############################################################################

    def agrega(self, x):

        row = x.row()

        a = self.model.record(row)

        for i in range(0, a.count()):

            print(a.value(i))
        if self.chequeo(a) is False:
            if a.value(7) != 'Pagado':
                columns = a.count()

                row = self.t.rowCount()

                self.t.insertRow(row)
                self.t.setItem(row, 0, QtWidgets.QTableWidgetItem(str(a.value(0))))
                self.t.setItem(row, 1, QtWidgets.QTableWidgetItem(str(a.value(1))))
                self.t.setItem(row, 2, QtWidgets.QTableWidgetItem(str(a.value(3))))
                self.t.setItem(row, 3, QtWidgets.QTableWidgetItem(str(a.value(5))))
                self.t.setItem(row, 4, QtWidgets.QTableWidgetItem(str(a.value(6))))
                self.t.setItem(row, 5, QtWidgets.QTableWidgetItem(str(a.value(2))))
#                self.t.setItem(row, 5, QtWidgets.QTableWidgetItem(a.value(6)))
                self.cuenta = self.cuenta + a.value(5)
                self.total.setText(str(self.cuenta))

##############################################################################

    def quita(self, x):

        valor = self.t.item(x.row(),2).text()
        self.cuenta = self.cuenta - float(valor)
        self.total.setText(str(self.cuenta))
        self.t.removeRow(x.row())

##############################################################################

    def cobra(self):
        if self.t.rowCount() > 0:
            self.recibos()
            util = Utilidades()
            sql = "UPDATE cuentas SET estado = 'Pagado' WHERE id = :ide"
            q = QtSql.QSqlQuery(self.db.database('Cooperadora'))
            q.prepare(sql)

            rows = self.t.rowCount()
            for i in range(0, rows):
                ide = int(self.t.item(i, 0).text())

                q.bindValue(":ide", ide)
                ej = util.ejecuto(q, 'Cooperadora')
            self.model.select()
            self.t.setRowCount(0)
##############################################################################

    def recibos(self):
        rows = self.t.rowCount()
        importe = 0
        detalle = ''
        dni = int(self.t.item(0,5).text())
        sql = "SELECT Nombre, Domicilio, numero, piso, depto, Localidad from alumnos WHERE DNI = :dni"
        q = QtSql.QSqlQuery(self.db.database('Cooperadora'))
        q.prepare(sql)
        q.bindValue(":dni", dni)
        util = Utilidades()
        ej = util.ejecuto(q,'cooperadora')
        while ej.next():
            nombre = ej.value(0)
            direccion = ej.value(1) + " " + str(ej.value(2)) + " " + ej.value(3) + " " + ej.value(4) + " - " + ej.value(5)


        for i in range(0, rows):
            detalle = detalle + self.t.item(i, 4).text() + " período "\
            + self.t.item(i, 2).text() + ".\n"
            valor = self.t.item(i, 3).text()
            valor = float(valor)
            importe = importe + valor

        '''Creo el recibo'''
        sql = "INSERT INTO recibos (Nombre, Detalle, Importe, fecha, Domicilio, DNI) VALUES "\
        "(:nom, :det, :imp, CURDATE(), :dom, :dni)"
        q = QtSql.QSqlQuery(self.db.database('Cooperadora'))
        q.prepare(sql)
        q.bindValue(":nom", nombre)
        q.bindValue(":det", detalle)
        q.bindValue(":imp", importe)
        q.bindValue(":dom", direccion)
        q.bindValue(":dni", dni)
        ej = util.ejecuto(q, 'Cooperadora')

        '''Obtengo el nùmero de recibo'''
        sql = "SELECT id from recibos WHERE Nombre = :nom AND Importe "\
        "= :imp ORDER by id DESC LIMIT 1"
        q.prepare(sql)
        q.bindValue(":nom", nombre)
        q.bindValue(":imp", importe)
        ej = util.ejecuto(q, 'Cooperadora')
        if ej.size() > 0:

            while ej.next():
                self.nroRecibo = ej.value(0)
                '''Imprimo o no el recibo'''
                re = util.MensajeOkNo("¿Deseas imprimir el recibo?")
                ok = re.exec_()

                if ok == 1024:
                    self.imprimo()
            '''Obtengo el saldo de caja e ingreso los movimientos a la'''\
            ''' caja discriminando movimiento'''
            for i in range(0, rows):
                sql = "SELECT saldo FROM caja ORDER BY idMovimiento DESC LIMIT 1"
                q = QtSql.QSqlQuery(self.db.database('Cooperadora'))
                q.prepare(sql)
                ej = util.ejecuto(q, 'Cooperadora')
                saldo = 0
                detalle = self.t.item(i, 4).text()
                importe = self.t.item(i, 3).text()
                importe = float(importe)

                '''Busco el codigo de la asignatura y si es mayor a 55'''\
                ''' le doy tipo b al movimiento'''
                tipo = self.tipoGasto(detalle)
                print (tipo)
                if ej.size() > 0:
                    while ej.next():
                        saldo = ej.value(0)

                saldo = saldo + importe

                '''Agrego el importe pagado a la caja'''
                sql = "INSERT INTO caja (Importe, Saldo, Detalle, recibo, "\
                "fecha, tipo) "\
                "VALUES (:imp, :saldo, :det, :recibo, CURDATE(), :tipo)"
                q.prepare(sql)
                q.bindValue(":saldo", saldo)
                q.bindValue(":det", detalle)
                q.bindValue(":imp", importe)
                q.bindValue(":recibo", self.nroRecibo)
                q.bindValue(":tipo", tipo)

                ej = util.ejecuto(q, 'Cooperadora')




##############################################################################

    def chequeo(self, a):

        rows = self.t.rowCount()

        existe = False
        if rows > 0 :
            for i in range(0, rows):

                if str(a.value(0)) == self.t.item(i,0).text():
                    existe = True
        return existe

##############################################################################

    def imprimo(self):
        datos = []
        util = Utilidades()
        '''Obtengo los datos del recibo y los envío a imprimir'''
        sql = "SELECT * from recibos WHERE id = :recibo"
        q = QtSql.QSqlQuery(self.db.database('Cooperadora'))
        q.prepare(sql)
        q.bindValue(":recibo", self.nroRecibo)
        ej = util.ejecuto(q,'Cooperadora')
        if ej.size() > 0:
            while ej.next():
                for i in range(ej.record().count()):
                    datos.append(ej.value(i))
        recibo = Recibo()
        recibo.creaRecibo(datos)

##############################################################################

    def tipoGasto(self, n):
        print("Imprimo nombre " + n)

        util = Utilidades()
        '''Obtengo los datos del recibo y los envío a imprimir'''
        sql = "SELECT id_asignatura from asignaturas WHERE Nombre = :tipo"
        q = QtSql.QSqlQuery(self.db.database('Cooperadora'))
        q.prepare(sql)
        q.bindValue(":tipo", n)
        pipi = q.executedQuery()
        print(pipi)
        tipo = 0
        ej = util.ejecuto(q,'Cooperadora')
        if ej.size() > 0:
            print("q es mayor a 0")
            while ej.next():
                print("entro al while")
                print(type(ej.value(0)))
                if ej.value(0) > 55:

                    tipo = 1
                else:
                    tipo = 0
        return tipo