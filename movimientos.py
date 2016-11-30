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
from impresiones import *
from listados import *


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
        self.mes.addItem('')
        self.mes.addItems(self.meses)

        '''QDateEdit Año'''
        self.anio = QtWidgets.QDateEdit()
        anio = QtCore.QDate().currentDate()
        self.anio.setDisplayFormat('yyyy')
        self.anio.setDate(anio)

        '''Combo Tipo Listado'''
        tipos = ["Tipo A", "Tipo B", "Docente"]
        self.tipo = QtWidgets.QComboBox()
        self.tipo.addItems(tipos)

        '''Combo Tipo de Movimiento'''
        mov = ["Ingresos", "Egresos"]
        self.mov = QtWidgets.QComboBox()
        self.mov.addItems(mov)

        self.layout = QtWidgets.QGridLayout()
        self.botonera = QtWidgets.QHBoxLayout()

        self.filtra = QtWidgets.QPushButton("Filtrar")
        self.CleanBtn = QtWidgets.QPushButton("Limpiar")
        self.recibo = QtWidgets.QPushButton("Imprimir")
        self.botonera.addWidget(self.filtra)
        self.botonera.addWidget(self.recibo)
        self.botonera.addWidget(self.CleanBtn)


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
        self.util.estiloTablas(self.model, self.caja)
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

        self.layout.addItem(self.top, 0, 0)
        self.ui.setLayout(self.layout)
        self.filtra.clicked.connect(self.filtrar)
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
        x = self.parentWidget()
        x.movimientos()

##############################################################################

    def doRecibo(self):
        imp = Impresion()
        tbl = self.Convierto_a_tabla(self.model.query())
        print(self.model.selectStatement())
        print(type(self.model.query()))
        for i in tbl:
            print(i)
        lbl = []
        for i in range(1, self.model.columnCount()):
            lbl.append(self.model.headerData(i, Qt.Horizontal, Qt.DisplayRole))

        formato = "portrait"
        size = A4

        t = self.toPdf(lbl, tbl)
        imp.creoEstilo()
        imp.creoStory()
        imp.agregoSpacer()
        imp.agregoTabla(t)
        imp.createPageTemplate(formato, size)
        imp.cierroStory()
        imp.imprimo()

##############################################################################

    def filtrar(self):
        txt = ''
        anio = self.anio.text()
        tipo = self.tipo.currentIndex()
        mov = self.mov.currentText()
        print(tipo)


        if self.mes.currentText() != '':
            mes = self.mes.currentText()
            mesnro = self.util.invDict(self.month)
            mesnum =  mesnro.get(mes)
            txt = txt + 'MONTH(fecha) = ' + str(mesnum)

        if txt == '':
            txt = txt + 'YEAR(fecha) = ' + str(anio)
        else:
            txt = txt + ' AND YEAR(fecha) = ' + str(anio)
        if tipo == 2:
            if txt == '':
                txt = txt + 'doc = 1'
            else:
                txt = txt + ' AND doc = 1'
        else:
            if txt == '':
                txt = txt + 'tipo = ' + str(tipo)
            else:
                txt = txt + ' AND tipo = ' + str(tipo)

        if mov == "Ingresos":
            if txt == '':
                txt = txt + 'Importe >= 0'
            else:
                txt = txt + ' AND Importe >= 0'

        else:
            if txt == '':
                txt = txt + 'Importe < 0'
            else:
                txt = txt + ' AND Importe < 0'

        self.model.setFilter(txt)
        self.model.select()


##############################################################################

    def toPdf(self, lbl, li, col=None):

        t = Table([lbl] + li, colWidths=col, rowHeights=None, style=None, splitByRow=1,
repeatRows=1, repeatCols=0, rowSplitRange=None, spaceBefore=None,
spaceAfter=None)
        t.setStyle(TableStyle([
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(3,0),'LEFT'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))
        return t

##############################################################################

    def Convierto_a_tabla(self, obj):
        '''Recibe un QtSqlQuery y devuelve una Lista de listas'''
        if isinstance(obj, QtSql.QSqlQuery):
            obj.seek(-1)
            l = []
            a = []

            while obj.next():

                l.append(obj.record())
            for i in l:

                b = []
                for r in range(i.count()):
                    if r != 0:
                        if isinstance(i.value(r), QtCore.QDate):
                            nac = i.value(r).toString("dd/MM/yyyy")
                            b.append(nac)
                        else:
                            b.append(i.value(r))
                a.append(b)
                b = None

            return a
        else:
            return "No me diste un Query"