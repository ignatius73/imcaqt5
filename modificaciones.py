import sys
#  import pymysql

from PyQt5 import QtCore, QtGui, uic, QtSql, QtWidgets
from asignaturas import *
from conn import *
from utilidades import *

class Modificaciones(QtWidgets.QWidget):
#Class Inscripciones - Inscribe a los alumnos.
    def __init__(self, usr):

        super(Modificaciones, self).__init__()
        '''Cargo el archivo ui'''
        print("modif1")
        self.ui = uic.loadUi("inscripcion3.ui", self)
        self.frm = QtWidgets.QFrame()
        self.sb = QtWidgets.QScrollArea()
        self.ui.lnCiclo.setText("2016")
        self.ui.lnCiclo.setDisabled(True)
        validator = QtGui.QIntValidator()
        self.ui.lnDni.setValidator(validator)
        self.ui.lnTel.setInputMask('999_9999_9999')
        self.ui.lnMov.setInputMask('999_99_9999_9999')
        self.ui.lnMail.setValidator
        print(self.lnDni.text())
        #  Instancio un objeto conexion
        self.usr = usr
        self.Conecto_a_DB()
        self.BtnOk.clicked.connect(self.ModificaAlumno)
        #  QtCore.QObject.connect(self.ui.Children(QtGui.QLineEdit), QtCore.SIGNAL("textChanged()"), self.IngresaAlumno)

##############################################################################

    def Cargo_Datos_Alumno(self, dni):
        print("entro")
        self.dni = dni
        print(self.dni)
        '''Obtengo datos del alumno a modificar'''
        sql = "SELECT * FROM alumnos WHERE DNI = :dni"
        q = QtSql.QSqlQuery(self.db.database("inscripciones"))
        print("pase el query")
        q.prepare(sql)
        q.bindValue(":dni", self.dni)
        ej = Utilidades()
        q = ej.ejecuto(q, "inscripciones")
        while q.next():
            self.lnNombre.setText(q.value(1))
            self.cBCarrera.setCurrentText(q.value(23))
            self.lnCiclo.setText(str(q.value(24)))
            self.cBSexo.setCurrentText(q.value(22))
            self.sBEdad.setValue(q.value(5))
            self.lnDni.setText(str(q.value(2)))
            print(type(q.value(4)))
            self.dENac.setDate(q.value(4))
            self.lnLugar.setText(q.value(3))
            self.ui.lnNac.setText(q.value(26))
            self.cBCivil.setCurrentText(q.value(10))
            self.cBHijos.setCurrentText(str(q.value(27)))
            self.lnFamiliar.setText(q.value(28))
            self.lnCalle.setText(q.value(6))
            self.lnNum.setText(str(q.value(7)))
            self.lnPiso.setText(q.value(8))
            self.lnDepto.setText(q.value(9))
            self.lnLocal.setText(q.value(11))
            self.lnPartido.setText(q.value(12))
            self.lnCP.setText(q.value(13))
            self.lnTel.setText(str(q.value(14)))
            self.lnMov.setText(str(q.value(15)))
            self.lnMail.setText(q.value(29))
            self.lntitulo.setText(q.value(16))
            self.dEEgr.setDate(q.value(30))
            self.lnEscuela.setText(q.value(32))
            self.lnDistrito.setText(q.value(33))
            self.lnOtros.setText(q.value(31))


##############################################################################

    def ModificaAlumno(self):
        pass

##############################################################################

    '''    def IngresaAlumno(self):
        print(self.lnDni.text())
        edits = self.ui.findChildren(QtWidgets.QLineEdit)
        self.lnNombre.text()
        self.cBCarrera.currentText()
        self.lnCiclo.text()
        self.cBSexo.currentText()
        self.sBEdad.text()
        self.lnDni.text()
        self.dENac.text()
        self.lnLugar.text()
        self.ui.lnNac.text()
        self.cBCivil.currentText()
        self.cBHijos.currentText()
        self.lnFamiliar.text()
        self.lnCalle.text()
        self.lnNum.text()
        self.lnPiso.text()
        self.lnDepto.text()
        self.lnLocal.text()
        self.lnPartido.text()
        self.lnCP.text()
        self.lnTel.text()
        self.lnMov.text()
        self.lnMail.text()
        self.lntitulo.text()
        self.dEEgr.text()
        self.lnEscuela.text()
        self.lnDistrito.text()
        self.lnOtros.text()
        self.lnInsti1.text()
        self.lnInsti2.text()
        if self.rBtnSi.isChecked() == True:
            self.trab = 1
        else:
            self.trab = 0
        self.activ = self.lnAct.text()
        self.horario = self.lnHorario.text()
        self.os = self.lnOS.text()
        self.emergencia = self.lnTelEmer.text()
        if self.cBDni.isChecked():
            self.fotoDni = 1
        else:
            self.fotoDni = 0
        if self.cBTit.isChecked():
            self.fotoTit = 1
        else:
            self.fotoTit = 0
        if self.cBReg.isChecked():
            self.numReg = 1
        else:
            self.numreg = 0
        if self.cBFoto.isChecked():
            self.fotos = 1
        else:
            self.fotos = 0
        if self.cBCert.isChecked():
            self.certif = 1
        else:
            self.certif = 0
        if self.validar_vacios(self.ui.lnDni):
            self.Insertar()
        else:
            self.repaint()'''

##############################################################################

    def Insertar(self):
        print("entro a insertar")
        # db = self.db.CreateConnection(self.usr, self.passw)
        #  Obtengo un cursor de DB abierto
        print("Nombre de la conexión " + self.db.connectionName())
        #Obtengo listado de campos de la tabla
        campos = "SHOW COLUMNS from alumnos WHERE Field <> 'IdAlumnos' AND Field <> 'Apellido' AND Field <> 'cohorte' AND Field <> 'Grupo_Sanguineo' AND Field <> 'Ántitetanica' AND Field <> 'Presion_Arterial' AND Field <> 'Enfermedades' AND Field <> 'Tratamiento' AND Field <> 'alergias' AND Field <> 'foto'"
        print("Nombre de la conexión " + self.db.connectionName())
        if self.db.database('inscripciones').isOpen() is False:
            print("database está cerrada")
            q = QtSql.QSqlQuery(self.db.database('inscripciones'))
            q.prepare(campos)
            q.exec_()
        else:
            print("database está abierta")
        cadena = ""
        print("entro al while")
        while q.next():
            cadena = cadena + q.value(0) + ", "
        total = len(cadena.rstrip())
        cadena1 = cadena[0:total -1]
        print("Cadena " + cadena1)

        #Preparo la cadena sql
        values = ":nombre, :dni, :lugar, :fenac, :edad, :calle, :numero, :piso, :depto, :civil, :local, :partido, :cp, :tel, :mov, :ecurs, :otros, :trab, :activ, :emer, :os, :sexo, :carrera, :anio, :lunac, :hijos, :flia, :mail, :egreso, :insti, :escuela, :distri, :doc_dni, :doc_Tit, :doc_reg, :doc_fot, :doc_cert"
        #sql = "INSERT INTO alumnos (" + cadena1 + ") VALUES (:nombre, :dni, :lugar, :fenac, :edad, :calle, :numero, :piso, :depto, :civil, :local, :partido, :cp, :tel, :mov, :ecurs, :otros, :trab, :activ, :emer, :os, :sexo, :carrera, :anio, :lunac, :hijos, :flia, :mail, :egreso, :insti1, :insti2, :escuela, :distri, :doc_dni, :doc_Tit, :doc_reg, :doc_fot, :doc_cert)"
        sql = "INSERT INTO alumnos(" + cadena1 + ") VALUES (" + values + ")"
        print(" Este sql " + sql)
        # sql = "INSERT INTO alumnos(Nombre, DNI, Lugar_Nacimiento, Fecha_Nacimiento, Edad, Domicilio, numero, piso, depto, Estado_Civil, Localidad, Partido, CP, Telefono, Celular, Estudios_Cursados, Otros, Trabaja, Ocupacion, emergencias, osocial, Sexo, Carrera, ciclo, Nacionalidad, hijos, acargo, mail, egreso, insti_otros, escuela, distrito, doc_dni, doc_Tit, doc_Reg, doc_fot, doc_cert) VALUES (:nombre, :dni, :lugar, :fenac, :edad, :calle, :numero, :piso, :depto, :civil, :local, :partido, :cp, :tel, :mov, :ecurs, :otros, :trab, :activ, :emer, :os, :sexo, :carrera, :anio, :lunac, :hijos, :flia, :mail, :egreso, :insti, :escuela, :distri, :doc_dni, :doc_Tit, :doc_reg, :doc_fot, :doc_cert)"  # , Fecha_Nacimiento, Edad, Domicilio, numero, piso, depto, Estado_Civil, Localidad, Partido, CP, Telefono, Celular, Estudios_Cursados, Otros, Trabaja, Ocupacion, emergencias, osocial, Sexo, Carrera, ciclo, Nacionalidad, hijos, acargo, mail, egreso, insti_otros, escuela, distrito, doc_dni, doc_Tit, doc_Reg, doc_fot, doc_cert) VALUES (:nombre,:dni,:lugar,:fenac,:edad,:calle,:numero,:piso,:depto,:civil,:local,:partido,:cp,:tel,:mov,:ecurs,:otros,:trab,:activ,:emer,:os,:sexo,:carrera,:anio,:lunac,:hijos,:flia,:mail,:egreso,:insti,:escuela :distri :doc_dni :doc_Tit :doc_reg :doc_fot)"'''
        #Creo el objeto para hacer la consulta
        print("Nombre de la conexión " + self.db.connectionName())
        q = QtSql.QSqlQuery(self.db.database('inscripciones'))
        q.prepare(sql)
        q.bindValue(":nombre", self.Nombre)
        q.bindValue(":dni", self.dni)
        q.bindValue(":lugar", self.lnNa)
        q.bindValue(":fenac", self.fenac)
        q.bindValue(":edad", self.edad)
        q.bindValue(":calle", self.calle)
        q.bindValue(":numero", self.numero)
        q.bindValue(":piso", self.piso)
        q.bindValue(":depto", self.depto)
        q.bindValue(":civil", self.civil)
        q.bindValue(":local", self.local)
        q.bindValue(":partido", self.partido)
        q.bindValue(":cp", self.cp)
        q.bindValue(":tel", self.tel)  # Validador
        q.bindValue(":mov", self.movil)  # validador
        q.bindValue(":ecurs", self.titulo)
        q.bindValue(":otros", self.otros)
        q.bindValue(":trab", self.trab)
        q.bindValue(":activ", self.activ)
        q.bindValue(":emer", self.emergencia)
        q.bindValue(":os", self.os)
        q.bindValue(":sexo", self.sexo)
        q.bindValue(":carrera", self.carrera)
        q.bindValue(":anio", self.anio)
        q.bindValue(":lunac", self.lunac)
        q.bindValue(":hijos", self.hijos)
        q.bindValue(":flia", self.familia)
        q.bindValue(":mail", self.mail)
        q.bindValue(":egreso", self.egreso)
        institutos = self.insti1 + ", " + self.insti2
        q.bindValue(":insti", institutos)
        q.bindValue(":escuela", self.escuela)
        q.bindValue(":distri", self.distrito)
        print(self.fotoDni)
        q.bindValue(":doc_dni", self.fotoDni)
        q.bindValue(":doc_Tit", self.fotoTit)
        q.bindValue(":doc_reg", self.numreg)
        q.bindValue(":doc_fot", self.fotos)
        q.bindValue(":doc_cert", self.certif)
        '''q.bindValue(":hora", self.horario)'''
        if self.db.database('inscripciones').isOpen():
            print("Damned world")
        else:
            print(self.db.connectionName() + " esta abierta")
            q.prepare(sql)
        estado = q.exec_()
        pipi = q.executedQuery()
        if estado is True:
            print("tudobom")
            self.close()
        else:
            print("DNI " + self.dni)
            print(pipi)
            print((self.db.database('inscripciones').lastError()))



    def validar_vacios(self, i):
        #  Valido si el campo está vacío
        if i.text() == "":
            i.setStyleSheet("background-color: cyan")
            p = QtCore.QPoint()
            p.setX = 50
            p.setY = 82
            QtGui.QToolTip.showText(p, "No puede estar vacío", i)
            return False
        else:
            return True


##############################################################################

    def Conecto_a_DB(self):
        try:
            self.db
        except:
            conn = Connection()
            conn.SetUsuario(self.usr)
            self.db = conn.CreateConnection('inscripciones')
            if self.db.database('inscripciones').isOpen():
                print("Conexión exitosa a Asignaturas")

#Creamos la instancia para inciar app
#app = QtGui.QApplication(sys.argv)
#nstanciamos una VentanaPrincipal
#ventana = Inscripciones()
#muestro la ventana
#ventana.show()
#Ejecutamos la app
#app.exec_()
