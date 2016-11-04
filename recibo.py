import sys, os
from PyQt5 import QtSql, QtWidgets
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4, landscape
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageTemplate, BaseDocTemplate, Frame
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from numeros import *
from number_to_letter import *

class Recibo():

    def __init__(self):
        super(Recibo, self).__init__()

##############################################################################

    def creaRecibo(self, datos):
        for i in datos:
            print(i)
        '''Recibe un list con los datos del recibo'''
        self.datos = datos
        self.nombre = "Recibo_Nro_" + str(self.datos[0]) + ".pdf"
        print(self.nombre)
        c = canvas.Canvas("recibos/" + self.nombre, pagesize=landscape(A4))
        width, height = A4
        enc1 = [10,
            7.6,
            0.25,
            7.5,
            1,
            7.32,
            7.4,
            0.2,
            11.6,
            7.8,
            7.7,
            7.65,
            8,
            7.3,
            6
            ]
        enc2 = [440,
            7.6,
            6.25,
            7.5,
            7,
            7.32,
            7.4,
            6.2
            ]
        enc3 = [432]
        c.setLineWidth(0.1)
        c.rect(0, enc1[13]*inch, width=height, height=0.1, stroke=1, fill=1)
        c.rect(0, enc1[14]*inch, width=height, height=0.1, stroke=1, fill=1)
        c.setFont('Times-Roman', 9)
        c.drawString(240, enc1[1]*inch, 'Fecha:')


        c.setFont('Times-Roman', 9)
        c.drawString(680, enc1[1]*inch, 'Fecha:')


        '''Fechas'''
        c.drawString(292, 7.65*inch, str(self.datos[4].day()))
        c.drawString(330, 7.65*inch, str(self.datos[4].month()))
        c.drawString(365, 7.65*inch, str(self.datos[4].year()))
        c.drawString(735, 7.65*inch, str(self.datos[4].day()))
        c.drawString(770, 7.65*inch, str(self.datos[4].month()))
        c.drawString(805, 7.65*inch, str(self.datos[4].year()))

        '''Cuerpo'''
        c.saveState()
        c.setDash(4,2)

        c.drawString(20, 7.0*inch, 'Nombre:')
        c.line(60,7.0*inch,410, 7*inch)

        c.drawString(20, 6.4*inch, 'Domicilio:')
        c.line(60,6.4*inch,410, 6.4*inch)

        c.drawString(440, 7.0*inch, 'Nombre:')
        c.line(830,7*inch,480, 7*inch)


        c.drawString(440, 6.4*inch, 'Domicilio:')
        c.line(830,6.4*inch,480, 6.4*inch)

        c.setFont('Times-Roman',10)

        c.drawString(80, 7.03*inch, self.datos[1])
        c.drawString(500, 7.02*inch, self.datos[1])
        c.drawString(80, 6.43*inch, self.datos[5])
        c.drawString(500, 6.43*inch, self.datos[5])
#        c.line(475,7.0*inch,830, 7*inch)

        c.restoreState()


        '''Texto'''

        '''Convierto numero a letras'''
        num = number()

        if self.datos[3] > 999:
            pete = num.to_word(self.datos[3])
        else:
            num = Numeros()
            pete = num.numero_to_letras(self.datos[3])

        print(pete)

        c.saveState()
        c.setDash(4,2)
        c.drawString(20, 5.7*inch, 'Recibí(mos) la suma de pesos:')
#        c.line(140,5.7*inch,410, 5.7*inch)
        c.drawString(440, 5.7*inch, 'Recibí(mos) la suma de pesos:')
#        c.line(140,5.7*inch,410, 5.7*inch)
        c.setFont('Times-Roman',10)
        style = getSampleStyleSheet()
        p = Paragraph(pete, style['Normal'])
        p.wrapOn(c, 260, 300)
        p.drawOn(c, 1.99*inch, 5.65*inch)
        p.wrapOn(c,260, 300)
        p.drawOn(c, 7.99*inch, 5.65*inch)

        c.drawString(20, 4.7*inch, 'En concepto de pago de:')
#        c.line(140,5.7*inch,410, 5.7*inch)
        c.drawString(440, 4.7*inch, 'En concepto de pago de:')
        story = []
        story2 =[]
        pe = Paragraph(self.datos[2], style['Normal'])

        story.append(pe)
        story2.append(pe)

        f = Frame(130, 155, 270, 200, showBoundary=0)
        fe = Frame(550, 155, 270, 200, showBoundary=0)
        f.addFromList(story, c)
        fe.addFromList(story2,c)

        c.restoreState()

        c.setFont('Times-Roman', 9)
        c.drawString(240, enc1[12]*inch, 'RECIBO°:')
        c.setFont('Times-Roman', 13)
        c.drawString(360, enc1[12]*inch, str(self.datos[0]))
        c.setFont('Times-Roman', 9)
        c.drawString(680, enc1[12]*inch, 'RECIBO°:')
        c.setFont('Times-Roman', 13)
        c.drawString(790, enc1[12]*inch, str(self.datos[0]))
        c.rect(275, enc1[1]*inch, width=40, height=15.1, stroke=1, fill=0)
        c.rect(315, enc1[1]*inch, width=40, height=15.1, stroke=1, fill=0)
        c.rect(355, enc1[1]*inch, width=40, height=15.1, stroke=1, fill=0)

        c.rect(715, enc1[1]*inch, width=40, height=15.1, stroke=1, fill=0)
        c.rect(755, enc1[1]*inch, width=40, height=15.1, stroke=1, fill=0)
        c.rect(795, enc1[1]*inch, width=40, height=15.1, stroke=1, fill=0)
        c.setLineWidth(0.5)
        c.line((enc1[8]*inch)/4, 800, (enc1[8]*inch)/4, 526)
        c.line((enc1[8]*inch)/1.30, 800, (enc1[8]*inch)/1.30, 526)
        self.encabezado(c,enc1)
        self.encabezado(c,enc2)
        c.setLineWidth(0.2)
        c.setDash(4,2)
        c.line(height/2, 0, height/2, height)
        self.pie(c, enc1)
        self.pie(c, enc3)


        c.saveState()
        c.setFont('Times-Bold', 10)
        c.drawString(240, 130, 'TOTAL:')
        c.drawString(660, 130, 'TOTAL:')
        c.setFillColor(HexColor("#9C9C9C"))
        c.rect(310, 130, width=90, height=15.1, stroke=1, fill=1)
        c.rect(730, 130, width=90, height=15.1, stroke=1, fill=1)
        c.restoreState()
        c.setFont('Times-Bold', 12)
        c.drawString(340, 133, str(self.datos[3]))
        c.drawString(760, 133, str(self.datos[3]))

        c.saveState()
        c.setFont('Times-Bold', 7)
        c.drawString(20, 60, 'Firma y Sello:')
        c.drawString(440, 60, 'Firma y Sello:')
        c.showPage()
        c.save()
        self.imprimo()

##############################################################################

    def imprimo(self):
        try:
            sitemap = os.name
            if sitemap == 'posix':
                print('linux')
                os.system('evince recibos/' + self.nombre)
            else:
                print('win')
                os.system("start AcroRD32 recibos/" + self.nombre + " &")
        except:
            print("No está instalado el evince")

##############################################################################

    def encabezado(self, canvas,m):
        ancho, alto = A4
        canvas.saveState()

        fonts = canvas.getAvailableFonts()
        for i in fonts:
            print(i)
        canvas.drawImage("logo_imca.png", m[0], m[1]*inch, width=180, height=50)
#        canvas.drawImage("logo_imca.png", m[0], m[1]*inch, width=200, height=100)
        canvas.setFont('Helvetica',8)
        canvas.setFillColor(colors.black)
        canvas.drawString(m[2]*inch, m[3]*inch, 'Instituto Municipal de Cerámica de Avellaneda')
        canvas.drawString(m[4]*inch, m[6]*inch, '"Emilio Villafañe"')
        canvas.setFont('Helvetica',5)
        canvas.drawString(m[7]*inch, m[5]*inch, 'Dependiente de la Secretaría '\
        'de Educación, Cultura y Promoción de las Artes')
        #A4[1]-50

        canvas.restoreState()

##############################################################################

    def pie(self, canvas, m):
        canvas.saveState()
        canvas.setFont('Times-Roman',7.7)
        canvas.drawString(m[0], 0.35 * inch, "Av. Mitre 2724, Avellaneda "\
        "(B1872GFF) Provincia de Buenos Aires. Telefax. 0054-11-4204-8223"\
        "/6378 D I P R E G E P 7 5 7 8")
        canvas.restoreState()

##############################################################################

    def datos(self, canvas, datos, d):
        canvas.saveState()
        canvas.setFont('Times-Roman',7.7)
        canvas.drawString(m[0], 0.25 * inch, "Av. Mitre 2724, Avellaneda "\
        "(B1872GFF) Provincia de Buenos Aires. Telefax. 0054-11-4204-8223"\
        "/6378 D I P R E G E P 7 5 7 8")
        canvas.restoreState()