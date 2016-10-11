import sys, os
from PyQt5 import QtCore, QtGui, uic, QtSql, QtWidgets
from asignaturas import *
from conn import *
from datetime import datetime, date, time, timedelta
from calificaciones import *
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush, QFont, QPageLayout
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QRectF, QLineF, QPoint
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsTextItem
from PyQt5.QtPrintSupport import QPrinter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4, landscape
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors

class Listados(QtWidgets.QWidget):

    def __init__(self, usr):
        super(Listados, self).__init__()
        self.usr = usr

    def Seleccion_Listado(self):
        '''Creo el Layout en donde presento los combos para seleccionar''' \
        '''el tipo de listado a imprimir'''

        self.layout = QtWidgets.QFormLayout()
        self.cbo = QtWidgets.QComboBox()

        listados = ['', 'Alumnos FOBA', 'Alumnos Tecnicatura', 'Alumnos Profesorado', 'Listados de Asistencia', 'Listar Alumnos por Cohorte']
        self.cbo.addItems(listados)
        self.layout.addRow("¿Qué tipo listado deseas?",self.cbo)
        self.Listo()
        self.lay2 = QtWidgets.QHBoxLayout()
        self.BtnListar = QtWidgets.QPushButton('Listar')
#        self.lay2.addStretch()
        self.lay2.addWidget(self.BtnListar)
        self.layout.addItem(self.lay2)
        self.setLayout(self.layout)
        self.BtnListar.clicked.connect(self.Listar)

    def onActivated(self):
        txt = self.cbo.currentIndex()
        print("Activated " + str(txt))
        if txt == 1:
            '''Listado FOBA'''
            self.Listar(txt)
        elif txt == 2:
            '''Listado Tecnicatura'''
            self.Listar('Tecnicatura')
        elif txt == 3:
            '''Listado Profesorado'''
            self.Listar('Profesorado de Artes Plásticas')
        elif txt == 4:
            '''Listado por asignaturas'''
            self.ListarAsistencias()
        elif txt == 5:
            self.ListarCohorte()
        elif txt == 6:
            self.Listar('Cursos Extraprogramáticos')

##############################################################################

    def Listo(self):
        self.cbo_anio = QtWidgets.QComboBox()
        a = datetime.now()

        rg = range((a.year-5), (a.year+10), 1)
        for i in rg:
            self.cbo_anio.addItem(str(i))
        self.cbo_anio.setCurrentText(str(a.year))
        self.layout.addRow("Seleccioná el año", self.cbo_anio)

##############################################################################

    def Listar(self, txt):
        txt = self.cbo.currentIndex()
        util = Utilidades()
        '''Instancio un objeto Connection'''
        conn = Connection()
        '''Obtengo un Cursor'''
        self.db = conn.conecto_a_DB(self.usr, 'Listados')
        print(txt)
        if txt == 1:
            sql = "SELECT Nombre, DNI, Edad, Domicilio, Celular FROM alumnos "\
            "WHERE cohorte is NULL"
            col = 5
            self.labels = ['Nombre', 'Dni', 'Edad', 'Domicilio', 'Celular']
        q = QtSql.QSqlQuery(self.db.database('Listados'))
        q.prepare(sql)
        estado = util.ejecuto(q, self.db)
        self.lista = util.Convierto_a_tabla(q)
        self.table = util.CreoTabla(q, self.labels)
#        self.Imprimir()
#        self.Imprimir2()
        self.toPdf()
#        self.imprimo()
#        imprimo = Calificaciones()
#        imprimo.Imprimir()

##############################################################################

    def imprimo(self):
        prt = QtPrintSupport.QPrinter()
        dialog = QtPrintSupport.QPrintDialog(prt, self)
        if(dialog.exec_() != QtWidgets.QDialog.Accepted):
            return
#        self.table.adjustSize()
        printLabel = self.table

        painter = QtGui.QPainter(prt)

        printLabel.render(painter)
        painter.end()

############################################################################

    def Imprimir(self):
        '''Imprime el objeto en table'''
        obj = QtWidgets.QGraphicsView()
        obj.setSceneRect(QRectF(obj.viewport().rect()))
        obj.scene = QGraphicsScene()
#        obj.scene.addItem
        f = QtGui.QFont("Arial", 6, QFont.Normal)
        lbl = QtWidgets.QLabel("Instituto Municipal de Cerámica de Avellaneda")
        lbl.setStyleSheet("background-color: #fefefe ")
        lbl.setFont(f)

        logo = QtGui.QPixmap("index.jpe")
        logo2 = logo.scaled(128, 128, QtCore.Qt.KeepAspectRatio)
#        lbl.setPixmap(logo2)
#        lbl.resize(180, 16)
        obj.scene.addWidget(lbl)
#        obj.scene.addWidget(self.table)
        qp = QPainter()
        prt = QtPrintSupport.QPrinter()

        prt.setPageOrientation(QPageLayout.Landscape)

        dialog = QtPrintSupport.QPrintDialog(prt, self)
        if(dialog.exec_() != QtWidgets.QDialog.Accepted):
            return

        printLabel = obj

        painter = QtGui.QPainter(prt)
        printLabel.render(painter)
        painter.end()

##############################################################################

    def Imprimir2(self):
        '''Imprime el objeto en table'''
        '''        obj = QtWidgets.QGraphicsView()
        obj.setSceneRect(QRectF(obj.viewport().rect()))
        obj.scene = QGraphicsScene()
        pen = QPen(Qt.black)
        brush = QBrush(Qt.Dense6Pattern)
        ft = QFont()
        ft.Helvetica
        obj.scene.
        (10, )
        obj.scene.addLine(QLineF(0, 0, 0, 1.0), pen).setPos(0,10)'''

        prt = QtPrintSupport.QPrinter()
        dialog = QtPrintSupport.QPrintDialog(prt, self)


        qp = QPainter(prt)
        qp.begin()
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(128, 250, 25, 255))
        pen.setStyle(Qt.DotLine)
        qp.setPen(pen)
        qp.drawLine(QPoint(10, 10), QPoint(1280 - 10, 10))

        # Dibujar segunda linea
        color = QColor()
        color.setNamedColor('#c2h6b4')

        pen.setColor(color)
        pen.setStyle(Qt.DashLine)

        qp.setPen(pen)
        qp.drawLine(QPoint(10, 10 + 20), QPoint(1280 - 10, 10 + 20))
        if(dialog.exec_() != QtWidgets.QDialog.Accepted):
            return

#        printLabel = qp

#        painter = QtGui.QPainter(prt)
#        printLabel.render(qp)
        prt.newPage()
        qp.end()

##############################################################################

    def toPdf(self):

#        doc = SimpleDocTemplate("test.pdf", pagesize = A4, orientation = landscape)
#        story=[]
        c = canvas.Canvas("test1.pdf")
        c.setPageSize(landscape(A4))

#        width, height = A4
#        a = drawString(1*inch,1*inch,"Welcome to Reportlab!"))
#        story.append(drawImage("index.jpg", 0.1*inch, 7.2*inch, width=70, height=45))
#        c.setFont("Helvetica", 12)
#        story.append(drawString(1.6*inch, 2*inch, "Instituto Municipal de Cerámica de Avellaneda"))
        t = Table([self.labels] + self.lista, colWidths=1*inch, rowHeights=None, style=None, splitByRow=1,
repeatRows=1, repeatCols=0, rowSplitRange=None, spaceBefore=None,
spaceAfter=None)
        t.setStyle(TableStyle([
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(3,0),'CENTER'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))
#        story.append(t)
#        doc.build(story)
#        os.system("/home/ignatius/imcaqt5/imcaqt5/test.pdf")
         #Establecemos el tamaño de la hoja que ocupará la tabla
        t.wrapOn(c, 800, 600)
        y = 200
        #Definimos la coordenada donde se dibujará la tabla
        t.drawOn(c, 60,y)
        c.showPage()
        c.save()