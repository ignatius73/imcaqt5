import sys, base64
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from utilidades import *
from conn import *


class Login(QtWidgets.QDialog):

    def __init__(self):
            super(Login, self).__init__()
            self.ui = uic.loadUi("login.ui", self)
            self.ui.OkBtn.setFocus()
            self.ui.OkBtn.clicked.connect(self.valida)
            self.ui.CancelBtn.clicked.connect(self.cancelar)

            self.exec_()

    def cancelar(self):
        exit()

    def valida(self):
        #Instancio una Conexión a la DB
        util = Utilidades()
        if util.validar_vacios(self.ui.lnUsuario):

            self.user = self.ui.lnUsuario.text()
            self.passwd = base64.b64encode(bytes(self.ui.lPass.text(), "utf-8"))

            #Construyo tupla para devolver a la ventana principal
            self.t = (self.user, self.passwd)
            self.close()
        else:
            self.repaint()

##############################################################################





