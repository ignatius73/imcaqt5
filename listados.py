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
from reportlab.lib.pagesizes import letter, A4, landscape, LEGAL
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from impresiones import *

class Listados(QtWidgets.QWidget):

    def __init__(self, usr):
        super(Listados, self).__init__()
        self.usr = usr
        self.conn = Connection()
        self.db = self.conn.conecto_a_DB(self.usr, 'Cooperadora')

    def Seleccion_Listado(self):
        '''Creo el Layout en donde presento los combos para seleccionar''' \
        '''el tipo de listado a imprimir'''
        self.layout = QtWidgets.QFormLayout()
        self.cbo = QtWidgets.QComboBox()
        self.model = QtSql.QSqlTableModel(None, self.db)
        listados = ['', 'Alumnos FOBA', 'Alumnos Tecnicatura', 'Alumnos Profesorado', 'Listados de Asistencia', 'Listar Alumnos por Cohorte']

        self.cbo.addItems(listados)
        self.layout.addRow("¿Qué tipo de listado deseas?",self.cbo)
        self.model.setTable('alumnos')
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
        for i in range(3,47):
            if i != 15 and i != 29:
                self.caja.hideColumn(i)
        util = Utilidades()
        util.estiloTablas(self.model, self.caja)
        self.caja.show()

        self.Listo()
        self.lay2 = QtWidgets.QVBoxLayout()
        self.BtnListar = QtWidgets.QPushButton('Listar')
#        self.lay2.addStretch()

        self.lay2.addWidget(self.caja)
        self.lay2.addWidget(self.BtnListar)
        self.lay2.setSpacing(8)
        self.layout.addItem(self.lay2)

        self.setLayout(self.layout)
        self.BtnListar.clicked.connect(self.Listar)
        self.cbo.activated.connect(self.onActivated)

##############################################################################

    def onActivated(self):
        self.limpioLay()
        txt = self.cbo.currentIndex()
        print("Activated " + str(txt))
        if txt == 2 or txt == 3:
            '''Tecnicatura o Profesorado'''
            self.porAnio()
        if txt == 4:
            '''Listado por asignaturas'''
            self.ListaXAsig()
        else:
            print("entro")


##############################################################################

    def Listo(self):
        self.cbo_anio = QtWidgets.QComboBox()
        a = datetime.datetime.now()
        rg = range((a.year-5), (a.year+10), 1)
        for i in rg:
            self.cbo_anio.addItem(str(i))
        self.cbo_anio.setCurrentText(str(a.year))
        self.layout.addRow("Seleccioná el año", self.cbo_anio)

##############################################################################

    def Listar(self, txt):
        curso = None
        dictanio = {1:'Primer', 2:'Segundo', 3:'Tercer', 4:'Cuarto'}
        print("Anio " + str(self.cbo_anio.currentText()))
        anio = self.cbo_anio.currentText()
        txt = self.cbo.currentIndex()
        util = Utilidades()
        '''Instancio un objeto Connection'''
        conn = Connection()
        '''Obtengo un Cursor'''
        self.db = conn.conecto_a_DB(self.usr, 'Listados')
        imp = Impresion()
        imp.creoEstilo()
        imp.creoStory()
        size = A4
        if txt == 1:
            sql = "SELECT distinct alumnos.Nombre, alumnos.DNI, "\
            "alumnos.Fecha_Nacimiento, alumnos.Edad, alumnos.Nacionalidad,"\
            " alumnos.Domicilio, alumnos.numero, alumnos.piso, alumnos.depto,"\
            " alumnos.Localidad, alumnos.Telefono, alumnos.Celular, "\
            "alumnos.mail FROM alumnos inner Join calificaciones on"\
            " alumnos.DNI = calificaciones.alumno inner join asignaturas "\
            "on calificaciones.id_asign = asignaturas.id_asignatura WHERE "\
            "alumnos.Carrera = 'Tecnicatura' AND "\
            "alumnos.cohorte IS NULL"
            col = 8
            self.labels = ['Nombre', 'Dni', 'F.Nacimiento', 'Edad',
            'Nacionalidad', 'Calle', 'Número', 'Piso', 'Depto', 'Localidad',
            'Tel. Fijo', 'Celular', 'Mail']
            formato = "landscape"
            txt1 = "Listado de Alumnos FOBA año " + self.cbo_anio.currentText()
            imp.definoEstilos()
            imp.agregoString(txt1)
            co = None
        elif txt == 2:
            curso = int(self.cbo2.currentText())
            sql = "SELECT distinct alumnos.Nombre, alumnos.DNI, "\
            "alumnos.Fecha_Nacimiento, alumnos.Edad, alumnos.Nacionalidad,"\
            " alumnos.Domicilio, alumnos.numero, alumnos.piso, alumnos.depto,"\
            " alumnos.Localidad, alumnos.Telefono, alumnos.Celular, "\
            "alumnos.mail FROM alumnos inner Join calificaciones on"\
            " alumnos.DNI = calificaciones.alumno inner join asignaturas "\
            "on calificaciones.id_asign = asignaturas.id_asignatura WHERE "\
            "alumnos.Carrera = 'Tecnicatura' AND "\
            "alumnos.cohorte IS NOT NULL AND alumnos.cohorte < :anio AND "\
            "asignaturas.anio = :ciclo"

            col = 8
            self.labels = ['Nombre', 'Dni', 'F.Nacimiento', 'Edad',
            'Nacionalidad', 'Calle', 'Número', 'Piso', 'Depto', 'Localidad',
            'Tel. Fijo', 'Celular', 'Mail']
            formato = "portrait"
            txt1 = "Listado de Alumnos Tecnicatura año " + self.cbo_anio.currentText()
            txt2 = dictanio[1]
            txt2 = txt2 + " Año"
            formato = "landscape"
            imp.definoEstilos()
            imp.agregoString(txt1)
            imp.agregoString(txt2)
            co = None
            size = LEGAL
        elif txt == 3:
            curso = int(self.cbo2.currentText())
            sql = "SELECT distinct alumnos.Nombre, alumnos.DNI, "\
            "alumnos.Fecha_Nacimiento, alumnos.Edad, alumnos.Nacionalidad,"\
            " alumnos.Domicilio, alumnos.numero, alumnos.piso, alumnos.depto,"\
            " alumnos.Localidad, alumnos.Telefono, alumnos.Celular, "\
            "alumnos.mail FROM alumnos inner Join calificaciones on"\
            " alumnos.DNI = calificaciones.alumno inner join asignaturas "\
            "on calificaciones.id_asign = asignaturas.id_asignatura WHERE "\
            "alumnos.Carrera = 'Profesorado de Artes Visuales' AND "\
            "alumnos.cohorte IS NOT NULL AND alumnos.cohorte < :anio AND "\
            "asignaturas.anio = :ciclo"

            col = 8

            self.labels = ['Nombre', 'Dni', 'F.Nacimiento', 'Edad',
            'Nacionalidad', 'Calle', 'Número', 'Piso', 'Depto', 'Localidad',
            'Tel. Fijo', 'Celular', 'Mail']
            formato = "landscape"
            txt1 = "Listado de Alumnos Profesorado de Artes Visuales "\
            "año " + self.cbo_anio.currentText()
            txt2 = dictanio[1]
            txt2 = txt2 + " Año"
            imp.definoEstilos()
            imp.agregoString(txt1)
            co = None
        elif txt == 4:
            '''Obtengo la asignatura a Listar'''
            self.txtxt = self.cbo2.currentText()
            sql = "SELECT DISTINCT alumnos.Nombre From alumnos INNER JOIN "\
            "calificaciones on calificaciones.alumno = alumnos.DNI INNER JOIN"\
            " asignaturas on calificaciones.id_asign = "\
            "asignaturas.id_asignatura WHERE asignaturas.nombre = :asig AND "\
            "calificaciones.nota IS NULL OR calificaciones.nota < 4"

            self.labels = ['Nombre Alumno', 'Fecha','Fecha','Fecha', 'Fecha','Fecha', 'Fecha', 'Fecha','Fecha']
            formato = "landscape"
            mes = QDate.currentDate()
            meses = util.meses()
            txt1 = str(self.txtxt)
            txt2 = "<br /> Listado de Asistencias <br />Mes de "  + str(meses.get(mes.month())) + " de " +  str(mes.year())
            imp.definoEstilos('Materia', 14, "Courier", 10)
            imp.agregoString(txt1, 'Materia')
            imp.definoEstilos('Listado', 12, "Courier-Bold", 16)
            imp.agregoString(txt2, 'Listado')
            co = 1.25*inch
        elif txt == 5:
            sql = "SELECT distinct alumnos.Nombre, alumnos.DNI, "\
            "alumnos.Fecha_Nacimiento, alumnos.Edad, alumnos.Nacionalidad,"\
            " alumnos.Domicilio, alumnos.numero, alumnos.piso, alumnos.depto,"\
            " alumnos.Localidad, alumnos.Telefono, alumnos.Celular, "\
            "alumnos.mail FROM alumnos inner Join calificaciones on"\
            " alumnos.DNI = calificaciones.alumno inner join asignaturas "\
            "on calificaciones.id_asign = asignaturas.id_asignatura WHERE "\
            "alumnos.cohorte =:anio"
            col = 8
            self.labels = ['Nombre', 'Dni', 'F.Nacimiento', 'Edad',
            'Nacionalidad', 'Calle', 'Número', 'Piso', 'Depto', 'Localidad',
            'Tel. Fijo', 'Celular', 'Mail']
            formato = "landscape"
            txt1 = "Listado de Alumnos Cohorte " + self.cbo_anio.currentText()
            imp.definoEstilos()
            imp.agregoString(txt1)
            co = None
        q = QtSql.QSqlQuery(self.db.database('Listados'))
        q.prepare(sql)
        if txt == 4:
            q.bindValue(":asig", self.txtxt)
        elif txt == 5:
            q.bindValue(":anio", self.cbo_anio.currentText())
        elif txt == 3:
            q.bindValue(":anio", self.cbo_anio.currentText())
            q.bindValue(":ciclo", curso)
        elif txt == 2:
            q.bindValue(":anio", self.cbo_anio.currentText())
            q.bindValue(":ciclo", curso)
        estado = util.ejecuto(q, self.db)

        self.lista = util.Convierto_a_tabla(q)
        self.table = util.CreoTabla(q, self.labels)
        t = self.toPdf(self.labels, self.lista, co)
        imp.agregoSpacer()
        imp.agregoTabla(t)
        imp.createPageTemplate(formato, size)
        imp.cierroStory()
        imp.imprimo()


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

        obj.scene.addWidget(lbl)

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
        prt.newPage()
        qp.end()

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

    def ListaXAsig(self):
        conn = Connection()
        util = Utilidades()
        '''Obtengo un Cursor'''
        self.db = conn.conecto_a_DB(self.usr, 'Listados')
        sql = "SELECT nombre from asignaturas"

        q = QtSql.QSqlQuery(self.db.database('Listados'))
        q.prepare(sql)
        estado = util.ejecuto(q, self.db)
        listados= []
        while estado.next():
            listados.append(estado.value(0))
        self.cbo2 = QtWidgets.QComboBox()
        self.cbo2.setObjectName("cbo2")
        self.cbo2.addItems(listados)
        '''Remuevo el self.lay2'''
        self.layout.removeItem(self.lay2)
        '''Agrego el Combo de listado de Asignaturas'''
        self.layout.addRow("Elegí la materia",self.cbo2)
#
#        self.layout.replaceWidget(self.BtnListar, self.cbo2)
        '''Vuelvo a agregar el lay2'''
        self.lay2.addWidget(self.BtnListar)
        self.layout.addItem(self.lay2)



##############################################################################

    def asistencias(self):
        print(self.cbo2.currentText())

##############################################################################

    def limpioLay(self):

        items = (self.layout.itemAt(i) for i in range(self.layout.count()))
        for i in items:
            if type(i) == QtWidgets.QWidgetItem:
                w = i.widget()
                if type(w) == QtWidgets.QLabel:
                    if w.text() == "Elegí la materia":
                        w.deleteLater()
                if type(w) == QtWidgets.QComboBox:
                    if w.objectName() == "cbo2":
                        w.deleteLater()

##############################################################################

    def porAnio(self):
        cant = []

        for i in range(1, 5):
            cant.append(str(i))

        self.cbo2 = QtWidgets.QComboBox()
        self.cbo2.setObjectName("cbo2")
        self.cbo2.addItems(cant)

        '''Remuevo el self.lay2'''
        self.layout.removeItem(self.lay2)
        '''Agrego el Combo de listado de Asignaturas'''
        self.layout.addRow("Elegí la materia",self.cbo2)
#
#        self.layout.replaceWidget(self.BtnListar, self.cbo2)
        '''Vuelvo a agregar el lay2'''
        self.lay2.addWidget(self.BtnListar)
        self.layout.addItem(self.lay2)
