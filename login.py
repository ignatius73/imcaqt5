import sys
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from utilidades import *
from conn import *

class Login(QtWidgets.QDialog):

    def __init__(self):
            super(Login, self).__init__()
            self.ui = uic.loadUi("login.ui", self)
            self.ui.lnUsuario.setText("root")
            self.ui.lPass.setText("schonberg")
            print("Esto esta en  el self" + self.ui.lnUsuario.text())
#            QtCore.QObject.connect(self.ui.OkBtn, QtCore.SIGNAL("clicked()"), self.valida)
            self.ui.OkBtn.clicked.connect(self.valida)
            self.ui.CancelBtn.clicked.connect(self.cancelar)
#            QtCore.QObject.connect(self.ui.CancelBtn, QtCore.SIGNAL("clicked()"), self.cancelar)
            self.exec_()

    def cancelar(self):
        exit()

    def valida(self):
        #Instancio una Conexión a la DB
        util = Utilidades()
        if util.validar_vacios(self.ui.lnUsuario):

            self.user = self.ui.lnUsuario.text()
            self.passwd = self.ui.lPass.text()
            #Construyo tupla para devolver a la ventana principal
            self.t = (self.user, self.passwd)
            self.close()
        else:
            self.repaint()

##############################################################################





