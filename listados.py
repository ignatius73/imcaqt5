import sys
from PyQt5 import QtCore, QtGui, uic, QtSql, QtWidgets
from asignaturas import *
from conn import *
from datetime import datetime, date, time, timedelta

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
        self.lay2.addStretch()
        self.lay2.addWidget(self.BtnListar)
        self.layout.addItem(self.lay2)
        self.setLayout(self.layout)
        self.BtnListar.clicked.connect(self.onActivated)

    def onActivated(self, txt):
        print(txt)
        if txt == 1:
            '''Listado FOBA'''
            self.Listar('FOBA')
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

    def Listo(self):
        self.cbo_anio = QtWidgets.QComboBox()
        a = datetime.now()

        rg = range((a.year-5), (a.year+10), 1)
        for i in rg:
            self.cbo_anio.addItem(str(i))
        self.cbo_anio.setCurrentText(str(a.year))
        self.layout.addRow("Seleccioná el año", self.cbo_anio)


