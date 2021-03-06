import sys, datetime
#  import pymysql

from PyQt5 import QtCore, QtGui, uic, QtSql, QtWidgets
from asignaturas import *
from conn import *
from PyQt5.QtCore import QDate, QVariant
from utilidades import *
from modificaciones import *



class Inscripciones(QtWidgets.QWidget):
#Class Inscripciones - Inscribe a los alumnos.
    def __init__(self, usr, dni):

        super(Inscripciones, self).__init__()
        '''Cargo el archivo ui'''
        self.ui = uic.loadUi("inscripcion4.ui", self)
        self.frm = QtWidgets.QFrame()
        self.sb = QtWidgets.QScrollArea()
        '''Si es noviembre o diciembre, pongo año actual'''
        hoy = QDate().currentDate()
        print(hoy.month())
        if hoy.month() == 11 or hoy.month() == 12:
            self.ui.lnCiclo.setText(str(hoy.year()+ 1))
        else:
            self.ui.lnCiclo.setText(str(hoy.year()))
        self.ui.lnCiclo.setDisabled(True)
        validator = QtGui.QIntValidator()
        reg = "[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,4}"
        r = QtCore.QRegExp()
        r.setPattern(reg)
        mailvalid = QtGui.QRegExpValidator(r, self)
        self.ui.lnDni.setValidator(validator)
        self.ui.lnNum.setValidator(validator)
        self.ui.lnTel.setValidator(validator)
        self.ui.lnMov.setValidator(validator)
        self.ui.lnMail.setValidator(mailvalid)

        self.dni = str(dni)
        self.lnDni.setText(self.dni)
        self.lnDni.setDisabled(True)
        #  Instancio un objeto conexion
        self.usr = usr
        self.Conecto_a_DB()
        self.BtnOk.clicked.connect(self.IngresaAlumno)
#        self.lnDni.editingFinished.connect(self.compruebaAlumno)

##############################################################################

    def IngresaAlumno(self):
        util = Utilidades()

        self.Nombre = self.lnNombre.text()
        self.carrera = self.cBCarrera.currentText()
        self.anio = self.lnCiclo.text()
        self.sexo = self.cBSexo.currentText()
        self.edad = self.sBEdad.text()
        self.dni = int(self.dni)
        self.fenac = util.convierte_Fechas(self.dENac.text())
        self.lunac = self.lnLugar.text()
        self.lnNa = self.ui.lnNac.text()
        self.civil = self.cBCivil.currentText()
        self.hijos = self.cBHijos.currentText()
        self.familia = self.lnFamiliar.text()
        self.calle = self.lnCalle.text()
        self.numero = self.IntONull(self.lnNum.text())
        self.piso = self.lnPiso.text()
        self.depto = self.lnDepto.text()
        self.local = self.lnLocal.text()
        self.partido = self.lnPartido.text()
        self.cp = self.lnCP.text()
        self.tel = self.IntONull(self.lnTel.text())
        self.movil = self.IntONull(self.lnMov.text())
        #self.movil = self.lnMov.text()

        self.mail = self.lnMail.text()
        self.titulo = self.lntitulo.text()
        self.egreso = self.dEEgr.text()
        self.escuela = self.lnEscuela.text()
        self.distrito = self.lnDistrito.text()
        self.otros = self.lnOtros.text()
        self.insti1 = self.lnInsti1.text()
        self.insti2 = self.lnInsti2.text()
        if self.rBtnSi.isChecked() is True:
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
            self.numReg = 0
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
            self.repaint()

##############################################################################

    def Insertar(self):
        #Obtengo listado de campos de la tabla'''
        campos = "SHOW COLUMNS from alumnos WHERE Field <> 'IdAlumnos' AND "\
        "Field <> 'Apellido' AND Field <> 'cohorte' AND Field <> "\
        "'Grupo_Sanguineo' AND Field <> 'Ántitetanica' AND Field <> "\
        "'Presion_Arterial' AND Field <> 'Enfermedades' AND Field <> "\
        "'Tratamiento' AND Field <> 'alergias' AND Field <> 'foto'"

        q = QtSql.QSqlQuery(self.db.database('inscripciones'))
        q.prepare(campos)
        q.exec_()
        cadena = ""
        print("entro al while")
        while q.next():
            cadena = cadena + q.value(0) + ", "
        total = len(cadena.rstrip())
        cadena1 = cadena[0:total -1]


        #Preparo la cadena sql
        values = ":nombre, :dni, :lunac, :fenac, :edad, :calle, :numero, "\
        ":piso, :depto, :civil, :local, :partido, :cp, :tel, :mov, :ecurs, "\
        ":otros, :trab, :activ, :emer, :os, :sexo, :carrera, :anio, :hora, "\
        ":lugar, :hijos, :flia, :mail, :egreso, :insti, :escuela, :distri, "\
        ":doc_dni, :doc_Tit, :doc_reg, :doc_fot, :doc_cert"
        sql = "INSERT INTO alumnos(" + cadena1 + ") VALUES (" + values + ")"

        '''sql = "INSERT INTO alumnos (Nombre, Carrera, ciclo, sexo, edad, DNI, "\
        "Fecha_Nacimiento, Lugar_Nacimiento,Nacionalidad, Domicilio, numero,"\
        "piso, depto, Estado_Civil, Localidad, Partido, CP, Telefono, Celular, "\
        "Estudios_Cursados, Otros, Trabaja, Ocupacion, emergencias, osocial, "\
        "hijos, acargo, mail, egreso, insti_otros, escuela, distrito, doc_dni,"\
        " doc_Tit, doc_reg, doc_fot, doc_cert, horario) "\
        "Values(:nombre, :carrera, :anio, :sexo, :edad, :dni, :fenac, "\
        ":lunac ,:lugar, :calle, :numero, :piso, :depto, :civil, :local, "\
        ":partido, :cp, :tel, :mov, :ecurs, :otros, :trab, :activ, :emer, :os"\
        ", :hijos, :flia, :mail, :egreso, :insti, :escuela, :distri, :doc_dni,"\
        " :doc_Tit, :doc_reg, :doc_fot, :doc_cert, :hora)"'''

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

        q.bindValue(":doc_dni", self.fotoDni)
        q.bindValue(":doc_Tit", self.fotoTit)
        q.bindValue(":doc_reg", self.numReg)
        q.bindValue(":doc_fot", self.fotos)
        q.bindValue(":doc_cert", self.certif)
        q.bindValue(":hora", self.horario)
        if self.db.database('inscripciones').isOpen():
            print("Damned world")
        else:
            print(self.db.connectionName() + " esta abierta")
            q.prepare(sql)
        estado = q.exec_()
        pipi = q.executedQuery()
        if estado is True:
            util = Utilidades()
            g = util.MensajeOkNo("El alumno " + self.Nombre + " fue "\
            "cargado correctamente. ¿Querés inscribirlo a las materias que "\
            "vaya a cursar?")
            res = g.exec_()

            if res == 1024:
                x = self.parentWidget()
                x.tudni = self.dni
                x.inscribe_a_asignaturas()

        else:
            util = Utilidades()
            g = util.Mensaje("Ocurrió un error al insertar el alumno. "\
            "Vuelve a intentarlo. Si el problema persiste comunicate con el "\
            "Administrador" + str(self.db.database('inscripciones').lastError()))


            g.exec_()


    def validar_vacios(self, i):
        #  Valido si el campo está vacío
        if i.text() == "":
            i.setStyleSheet("background-color: cyan")
            p = QtCore.QPoint()
            p.setX = 50
            p.setY = 82
            QtWidgets.QToolTip.showText(p, "No puede estar vacío", i)
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

##############################################################################

    def IntONull(self, ln):
        if ln == '':
            n = QVariant()
        else:
            n = int(ln)
        return n



#Creamos la instancia para inciar app
#app = QtGui.QApplication(sys.argv)
#nstanciamos una VentanaPrincipal
#ventana = Inscripciones()
#muestro la ventana
#ventana.show()
#Ejecutamos la app
#app.exec_()
