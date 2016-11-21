import sys

from PyQt5 import QtCore, QtGui, uic, QtSql, QtWidgets
from PyQt5.QtCore import QVariant
from conn import *
from utilidades import *


class Admin(QtWidgets.QWidget):

    def __init__(self):
        super(Admin, self).__init__()
        self.setMaximumHeight(650)
        self.sc = QtWidgets.QScrollArea()


    def CrearUsuario(self, usr):

        if usr[0] == "root":
            self.usr = usr
            self.Conecto_a_DB()
            self.Formulario()
        else:
            return

##############################################################################

    def Conecto_a_DB(self):
        try:
            self.db
        except:
            conn = Connection()
            conn.SetUsuario(self.usr)
            self.db = conn.CreateConnection('superadmin')
            if self.db.database('asignaturas').isOpen():
                pass

##############################################################################

    def Formulario(self):

        '''Cargo el archivo ui'''
        self.util = Utilidades()
        self.scroll = QtWidgets.QScrollBar()


        self.layIzq = QtWidgets.QVBoxLayout()
#        self.layIzq.setSpacing(5)

        self.layout = QtWidgets.QGridLayout()
        self.botonera = QtWidgets.QHBoxLayout()
        self.importe = QtWidgets.QLineEdit()
        self.concepto = QtWidgets.QLineEdit()

        self.agregar = QtWidgets.QPushButton("Agregar")
        self.CleanBtn = QtWidgets.QPushButton("Limpiar")
        self.recibo = QtWidgets.QPushButton("Recibo")

        self.botonera.addWidget(self.agregar)
        self.botonera.addWidget(self.recibo)
        self.botonera.addWidget(self.CleanBtn)

        self.lbl = QtWidgets.QLabel("Usuario")
        self.lbl2 = QtWidgets.QLabel("Contraseña")
        self.layIzq.addWidget(self.lbl)
        self.layIzq.addWidget(self.importe)
        self.layIzq.addWidget(self.lbl2)
        self.layIzq.addWidget(self.concepto)

        lay = QtWidgets.QVBoxLayout()

        self.gbtab = QtWidgets.QGroupBox("Tablas")
        tablas = ["alumnos", "asignaturas", "caja", "calificaciones","carreras", "cooperadora", "cuentas", "cursos", "recibos", "registros", "valores"]
        permisos = ["DELETE", "INSERT", "UPDATE", "SELECT"]
        f = 0
        for i in tablas:
            lay2 = QtWidgets.QGridLayout()
            self.gb = QtWidgets.QGroupBox("Permisos")
            ckbtab = QtWidgets.QCheckBox(i, self.gbtab)
            ckbtab.setObjectName(i)
            for i in permisos:

                ckb = QtWidgets.QCheckBox(i, self.gb)
                ckb.setObjectName(i)
                lay2.addWidget(ckb,0,f)
                f = f + 1
            self.gb.setLayout(lay2)

            lay2 = None
            lay.addWidget(ckbtab)
            lay.addWidget(self.gb)
            self.gb = None
        self.gbtab.setLayout(lay)


        self.layIzq.addWidget(self.gbtab)


        self.layIzq.addItem(self.botonera)




        self.setLayout(self.layIzq)
#        self.sc.setWidget(self)

#        self.agregar.clicked.connect(self.agrega)
#        self.CleanBtn.clicked.connect(self.limpia)
#        self.recibo.clicked.connect(self.doRecibo)