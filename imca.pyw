import sys
from PyQt5 import QtCore, QtGui, uic, QtSql, QtWidgets

from inscribirAlumno import *
from asignaturas import *
from conn import *
from utilidades import *
from login import *
from calificaciones import *
from listados import *
from modificaciones import *
from administracion import *
from registro import *
from caja import *
from movimientos import *
from alumnos import *
from superadmin import *


global c

c = 3

#Clase ventana principal
class VentanaPrincipal(QtWidgets.QMainWindow):
    #Modo constructor de la clase
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        #Obtengo usuario y contraseña
        #Creo tupla para usuario y contraseña
        if self.login() is True:
            #Creo un layout para el contenedor mainwindow
            self.ui = uic.loadUi("pymca.ui", self)
            self.dni = None
            self.registro()
            self.ui.action_Nuevo_Alumno.triggered.connect(self.calcular)
            self.ui.action_Listados.triggered.connect(self.modulo_Listados)
            self.ui.action_Salir.triggered.connect(self.salir)
            self.ui.actionCoo_peradora.triggered.connect(self.cooperadora)
            self.ui.actionCaja.triggered.connect(self.caja)
            self.ui.actionMovimientos.triggered.connect(self.movimientos)
            self.ui.action_Inicio.triggered.connect(self.alumnos)
            self.ui.actionCrear_Usuario.triggered.connect(self.crearUsuario)
            self.alumnos()
        else:
            global c
            c = c - 1

            if c != 0:
                self.__init__()
            else:
                exit()

##############################################################################

    def calcular(self, m=0):

        if m == 0:
            self.cargoDNI2()
            if self.tudni[0] != 0:

                self.dni = self.tudni[0]
                dni_exist = self.conn.ConsultoDNI(self.dni, self.db)
                if dni_exist is False:
                    self.hijo = Inscripciones(self.usuario, self.dni)
                    self.setCentralWidget(self.hijo)
                else:
                    v= Utilidades()
                    t = "El alumno ya se encuentra inscripto. ¿Querés modificarlo?"
                    fin = v.Confirmar(t)
                    if fin == 1024:
                        self.modifico_alumno(1)

        else:
            self.hijo = Inscripciones(self.usuario, self.dni)
            self.setCentralWidget(self.hijo)




##############################################################################

    def inscribe_a_asignaturas(self):

        if self.tudni != 0:
            self.dni = str(self.tudni)

            self.hijo = Asignaturas(self.usuario)
            dni_exist = self.conn.ConsultoDNI(self.dni, self.db)

            if dni_exist is True:
                lay = self.hijo.inscribir(self.dni)
                self.hijo.setLayout(lay)
                self.sb = QtWidgets.QScrollArea()
                self.setCentralWidget(self.hijo)

            else:
                v= Utilidades()
                t = "El Alumno no existe en nuestros registros. ¿Desea agregarlo?"
                fin = v.Confirmar(t)
                if fin == 1024:
                    self.calcular(1)
        else:
            print(self.tudni)


##############################################################################

    def cargoDNI(self):
        etiqueta = QtWidgets.QLabel("Ingrese DNI del Alumno")
        self.lnAlumno = QtWidgets.QLineEdit()
        validator = QtGui.QIntValidator()
        self.lnAlumno.setValidator(validator)
        OkBtn = QtWidgets.QPushButton('Acep&tar')
        CancelBtn = QtWidgets.QPushButton('Canc&elar')

        hbox = QtWidgets.QVBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(etiqueta)
        hbox.addWidget(self.lnAlumno)
        hbox.addStretch(1)


        hbox1 = QtWidgets.QHBoxLayout()

        hbox1.addStretch(2)
        hbox1.addWidget(OkBtn)
        hbox1.addWidget(CancelBtn)
        hbox1.addStretch(1)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(hbox1)

        self.dialog = QtWidgets.QDialog()
        self.dialog.setLayout(vbox)
        self.dialog.move(50, 50)
        self.dialog.resize(100, 100)
        OkBtn.clicked.connect(self.cargo)
        CancelBtn.clicked.connect(self.cancelo)
        self.dialog.exec_()

##############################################################################

    def cargoDNI2(self):
        ok = False
        self.tudni = QtWidgets.QInputDialog.getInt(self,"DNI", "Ingresa tu Documento")



##############################################################################

    def cancelo(self):
        self.dialog.close()
        return False

##############################################################################

#Devuelve self.dni
    def cargo(self):
        valido = Utilidades()
        if valido.validar_vacios(self.lnAlumno):
            self.dni = self.lnAlumno.text()
            self.dialog.close()
            return True
        else:
            self.dialog.repaint
            return

##############################################################################

#Conecto a la BD
    def login(self):
        login = Login()
        login.valida
        self.usuario = login.t
        self.conn = Connection()
        self.conn.SetUsuario(self.usuario)
        v = self.db = self.conn.CreateConnection('principal')
        if v is False:
            return False
        else:
            return True

##############################################################################

    def Cargo_Notas(self):

        if self.tudni != 0:
            self.hijo = Calificaciones(self.usuario)
            self.hijo.Listado(self.tudni)
            self.setCentralWidget(self.hijo)

##############################################################################

    def imprimo(self):
        prt = QtPrintSupport.QPrinter()
        dialog = QtPrintSupport.QPrintDialog(prt, self)
        if(dialog.exec_() != QtWidgets.QDialog.Accepted):
            return
        printLabel = self.hijo

        painter = QtGui.QPainter(prt)
        printLabel.render(painter)
        painter.end()

##############################################################################

    def modifico_alumno(self, m=0):

        if m==0:
#            self.cargoDNI2()
            if self.tudni != 0:
                self.dni = str(self.tudni)
                dni_exist = self.conn.ConsultoDNI(self.dni, self.db)
                if dni_exist is True:
                    self.hijo = Modificaciones(self.usuario)
                    self.hijo.Cargo_Datos_Alumno(self.dni)
                    self.setCentralWidget(self.hijo)
                else:
                    v= Utilidades()
                    t = "El Alumno no existe en nuestros registros. "\
                    "¿Desea agregarlo?"
                    fin = v.Confirmar(t)
                    if fin == 1024:
                       self.calcular(1)
        else:
            self.hijo = Modificaciones(self.usuario)
            self.hijo.Cargo_Datos_Alumno(self.dni)
            self.setCentralWidget(self.hijo)


##############################################################################

    def modulo_Listados(self):
        '''Cargo módulo de listados'''
        self.hijo = Listados(self.usuario)
        self.hijo.Seleccion_Listado()
        self.setCentralWidget(self.hijo)

##############################################################################

    def salir(self):
        self.close()

##############################################################################

    def cooperadora(self):
        '''Cargo formulario cooperadora'''
        self.hijo = Administracion(self.usuario)
        self.hijo.formularioCoop()
        self.setCentralWidget(self.hijo)

##############################################################################

    def registro(self):
        '''Costeo los cargos mensuales a los alumnos'''
        registro = Registro(self.usuario)
        registro.registra()

##############################################################################

    def caja(self):
        '''Cargo formulario de Caja'''
        if self.usuario[0] == 'root' or self.usuario[0] == "jana":
            self.hijo = Caja(self.usuario)
            self.hijo.formularioCaja()
            self.setCentralWidget(self.hijo)
        else:
            util = Utilidades()
            x = util.Mensaje("Usted no tiene permisos para ingresar"\
            " al módulo de caja")
            x.exec_()
##############################################################################

    def movimientos(self):
        '''Cargo formulario de Caja'''
        self.hijo = Movimientos(self.usuario)
        self.hijo.formularioCaja()
        self.setCentralWidget(self.hijo)

##############################################################################

    def alumnos(self):
        '''Cargo formulario de Caja'''
        self.hijo = Alumnos(self.usuario)
        self.hijo.formularioCaja()
        self.setCentralWidget(self.hijo)

##############################################################################

    def control(self, talumno):
        self.tudni = []
        self.tudni = int(talumno[1])
        if talumno[2] == "Modificar Alumno":
            self.modifico_alumno(0)
        elif talumno[2] == 'Agregar Calificaciones':
            self.Cargo_Notas()
        elif talumno[2] == 'Borrar Alumno':
            self.borrar_Alumno()
        elif talumno[2] == 'Inscribir Asignaturas':
            self.inscribe_a_asignaturas()


##############################################################################

    def borrar_Alumno(self):
        if self.tudni != 0:
            self.hijo = Alumnos(self.usuario)
            self.hijo.borrar_Alumno(self.tudni)
            self.alumnos()

##############################################################################

    def crearUsuario(self):
        self.hijo = Admin()
        self.hijo.CrearUsuario(self.usuario)
        self.setCentralWidget(self.hijo)


#Creamos la instancia para inciar app
app = QtWidgets.QApplication(sys.argv)
#nstanciamos una VentanaPrincipal
ventana = VentanaPrincipal()
ventana.move(0,0)
#muestro la ventana
ventana.show()
#Ejecutamos la app
app.exec_()