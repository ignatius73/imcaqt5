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
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageTemplate, BaseDocTemplate, Frame
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY

class Impresion():

    def __init__(self):
        super(Impresion, self).__init__()

##############################################################################

    def encabezadoLandscape(self, canvas, doc):
        ancho, alto = A4
        canvas.saveState()
        fonts = canvas.getAvailableFonts()
        for i in fonts:
            print(i)
        canvas.drawImage("logo_imca.png", 10, 7.2*inch, width=200, height=70)
        canvas.setFont('Helvetica',19)
        canvas.setFillColor(colors.black)
        canvas.drawString(3.5*inch, 7.7*inch, 'Instituto Municipal de ' \
        'Cerámica de Avellaneda "Emilio Villafañe"')
        canvas.setFont('Helvetica',10)
        canvas.drawString(3.5*inch, 7.5*inch, 'dependiente de la Secretaría '\
        'de Educación, Cultura y Promoción de las Artes')
        #A4[1]-50
        canvas.rect(0, 7*inch, width=alto, height= 0.1, stroke=1, fill=1)
        canvas.restoreState()

##############################################################################

    def encabezado(self, canvas, doc):
        ancho, alto = A4
        canvas.saveState()
        fonts = canvas.getAvailableFonts()
        for i in fonts:
            print(i)
        canvas.drawImage("logo_imca.png", 10, 10.5*inch, width=200, height=70)
        canvas.setFont('Helvetica',12)
        canvas.setFillColor(colors.black)
        canvas.drawString(3.2*inch, 11*inch, 'Instituto Municipal de ' \
        'Cerámica de Avellaneda "Emilio Villafañe"')
        canvas.setFont('Helvetica',8)
        canvas.drawString(3.2*inch, 10.8*inch, 'dependiente de la Secretaría '\
        'de Educación, Cultura y Promoción de las Artes')
        #A4[1]-50
        canvas.rect(0, 10.3*inch, width=ancho, height= 0.1, stroke=1, fill=1)
        canvas.restoreState()

##############################################################################

    def pie(self, canvas, doc):
        canvas.saveState()
        canvas.setFont('Times-Roman',9)
        canvas.drawString(inch, 0.75 * inch, "Page %d" % doc.page)
        canvas.restoreState()

##############################################################################

    def createPageTemplate(self, orientacion, size):

        self.doc = BaseDocTemplate("phello.pdf")
        self.doc.topMargin = 1*inch
        frameT = Frame(self.doc.leftMargin, self.doc.bottomMargin, self.doc.topMargin, self.doc.width, self.doc.height, showBoundary=1, id='normal')
        if orientacion == "landscape":
            self.doc.pagesize = landscape(A4)
            PTUnaColumna = PageTemplate(id='UnaColumna', frames=[frameT], onPage=self.encabezadoLandscape, onPageEnd=self.pie)


        else:
            self.doc.pagesize = A4
            PTUnaColumna = PageTemplate(id='UnaColumna', frames=[frameT], onPage=self.encabezado, onPageEnd=self.pie)
        PTUnaColumna.pageBreakBefore=0
        PTUnaColumna.keepWithNext=0
        self.doc.addPageTemplates([PTUnaColumna])

##############################################################################

    def creoEstilo(self):
        self.styles = getSampleStyleSheet()
        self.estilo1 = self.styles['BodyText']
        self.estilo2 = self.styles['Normal']

##############################################################################

    def creoStory(self):
        self.story = []



##############################################################################

    def cierroStory(self):
        self.doc.build(self.story)

##############################################################################

    def agregoString(self, txt):
        titulo = Paragraph(txt, self.styles['Normal'])
        self.story.append(titulo)

##############################################################################

    def definoEstilos(self):
        self.styles.add(ParagraphStyle(name = "Titulo",  alignment=TA_CENTER, fontSize=20, fontName="Helvetica-BoldOblique"))

##############################################################################

    def agregoTabla(self, t):
        self.story.append(t)

##############################################################################

    def imprimo(self):
        try:
            os.system('evince phello.pdf')
        except:
            print("No está instalado el evince")