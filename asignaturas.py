import sys
#..import pymysql

from PyQt5 import QtCore, QtGui, uic, QtSql, QtWidgets
from PyQt5.QtCore import QVariant
from conn import *
from utilidades import *
from impresiones import *
from listados import *
from reportlab.lib.pagesizes import letter, A4, landscape, LEGAL

class Asignaturas(QtWidgets.QWidget):
    '''La clase Asignaturas llevara adelante todas las operaciones ''' \
    '''referidas a inscripcion a Materias, y sus derivados'''
    def __init__(self, usr):
        super(Asignaturas, self).__init__()
        '''Instancio un objeto a la base de datos'''
        self.usr = usr
        self.Conecto_a_DB()

##############################################################################

    def inscribir(self, dni):
        '''Creo lista para guardar los GroupBox a recorrer'''

        self.lista = []
        self.v = QtWidgets.QVBoxLayout()


        '''Obtengo la consulta'''
        self.dni = dni
        q = self.ObtengoCalificaciones()

        if q.size() > 0:
            '''Proceso FOBA'''
            ctrl = 1
            layFoba = self.ListoFOBA(ctrl)

            if layFoba is True:
                layCarrera = self.anotoProfTec()
                self.lista.append(layCarrera)
            elif layFoba is False:
                print("No tienes materias disponibles para la inscripción")
            else:
                self.lista.append(layFoba)
            layCursos = self.ListoCursos()
            self.lista.append(layCursos)

        else:

            '''Solo puede anotarse a FOBA y a Cursos Extraprogramaticos'''
            layFoba = self.ListoFOBA()
            layCursos = self.ListoCursos()
            self.lista = [layFoba, layCursos]

        txt = QtWidgets.QLabel("Por favor, seleccioná las materias "\
        "a las que deseas inscribirte")
        self.v.addWidget(txt)
#        ly = QtWidgets.QVBoxLayout()
#        ly.addWidget(txt)

#        self.v.addLayout(ly)
        for i in self.lista:
            self.v.addWidget(i)

        h = QtWidgets.QHBoxLayout()
        BtnOk = QtWidgets.QPushButton("&Anotar")
        BtnCancel = QtWidgets.QPushButton("&Limpiar")
        h.addStretch(1)
        h.addWidget(BtnOk)
        h.addWidget(BtnCancel)
        self.v.addLayout(h)
        self.control = 0
        BtnOk.clicked.connect(self.anotar)
        return self.v

##############################################################################

    def ObtengoCalificaciones(self):
        '''Busco en la tabla de Calificaciones las materias no aprobadas aún por el dni'''
        sql = "SELECT * from calificaciones WHERE alumno = :dni"
        if self.db.database('asignaturas').isOpen() is True:

            q = QtSql.QSqlQuery(self.db.database('asignaturas'))
            q.prepare(sql)
            q.bindValue(":dni", self.dni)
            estado = self.ejecuto(q)
            return estado
        else:

            print(self.db.database('asignaturas').lastError())

    def ListoMaterias(self, ctrl, c):
        pass

##############################################################################

    def ListoFOBA(self, control=0):
        '''Lista todas las posibilidades de presentación de materias FOBA''' \
        '''Devuelve un QGroupBox'''

        q = self.MateriasFoba(control)

        if q is True:

            return True
        elif isinstance(q, str):

            return False
        if isinstance(q, list):
            gl = self.CreoGridLista(q, "Materias FOBA")
        elif isinstance(q, QtSql.QSqlQuery):
            gl = self.CreoGrid(q, "Materias FOBA")
            gl.setObjectName("GFoba")

        return gl

##############################################################################

    def ListoCursos(self):
        '''Crea un GroupBox con todas las cursos disponibles''' \
        '''Devuelve un GroupBox'''
        q = self.CursosExtraprogramaticos()
        gl = self.CreoGridLista(q, "Cursos Extraprogramáticos")
        gl.setObjectName("GCursos")
        return gl

#########################################################################

    def CreoGridLista(self, q, titulo):
        '''Crea un GridLayout. Recibe un List y devuelve un GroupBox'''
        lay = QtWidgets.QGridLayout()
#        lay = QtWidgets.QVBoxLayout()
        lay.setObjectName(titulo)
        f = 0
        c = 0
        gb = QtWidgets.QGroupBox(titulo)
        for i in q:
            if c == 4:
                c = 0
                f = f + 1
            '''Creo el CheckBox y lo agrego al Layout'''
            ckb = QtWidgets.QCheckBox(i.value(1), gb)
            ckb.setObjectName(str(i.value(0)))

            lay.addWidget(ckb, f, c)
#            lay.addWidget(ckb)
            c = c + 1
            '''seteo el layout al grid'''
#        gb = QtGui.QGroupBox(titulo)

        gb.setLayout(lay)

        return gb

#############################################################################

    def CreoGrid(self, q, titulo):
        '''Crea un GridLayout. Recibe un QtSql.SqlQuery devuelve un GroupBox'''
        lay = QtWidgets.QGridLayout()
        lay.setObjectName(titulo)
        f = 0
        c = 0
        gb = QtWidgets.QGroupBox(titulo)
        while q.next():
            if c > 4:
                c = 0
                f = f + 1
                '''Creo el CheckBox y lo agrego al Layout'''
            ckb = QtWidgets.QCheckBox(q.value(1), gb)
            ckb.setObjectName(str(q.value(0)))

            lay.addWidget(ckb, f, c)
            c = c + 1
            '''seteo el layout al grid'''
#        gb = QtGui.QGroupBox(titulo)
        gb.setLayout(lay)
        return gb

##############################################################################

    def anotar(self):
        '''Ejecuta la consulta de inserción de materias para el alumno'''
        self.control = self.control + 1
        mat = []
        self.materias = []
        self.mat = []
        '''Obtengo largo de la lista'''
        for i in self.lista:
            if isinstance(i, QtWidgets.QGroupBox):
                for c in i.findChildren(QtWidgets.QCheckBox):
                    if c.isChecked():
                        mat.append(c.objectName())
                        self.mat.append(c.objectName())
                        self.materias.append("(")
                        self.materias.append(c.objectName())
                        self.materias.append(", ")
                        self.materias.append(self.dni)
                        self.materias.append(")")
                        self.materias.append(", ")
        self.materias.pop()
        l = "".join(self.materias)

        self.anotoMaterias(self.dni, l)
        self.AgregoFechaInscripcion()
        '''Obtengo el nombre del Alumno'''
        sql = "SELECT nombre from alumnos WHERE DNI = :dni"
        q = QtSql.QSqlQuery(self.db.database('asignaturas'))
        q.prepare(sql)
        q.bindValue(":dni", int(self.dni))
        estado = self.ejecuto(q)
        formato = "portrait"
        while estado.next():
            nombre = q.value(0)
        '''Obtengo la fecha actual'''
        fecha = QDate.currentDate()
        imp = Impresion()
        imp.creoEstilo()
        imp.creoStory()
        imp.definoEstilos()
        imp.agregoString("Inscripción a Materias")
        imp.agregoSpacer()
        imp.definoEstilos('txt', 10, "Helvetica", 12)
        txt = "Nombre del Alumno: " + nombre
        imp.agregoString(txt,'txt')
        txt = "Fecha de Inscripción: " + fecha.toString("dd-MM-yyyy")
        imp.agregoString(txt, 'txt')
        nomMat = []
        for i in mat:

            sql = "SELECT id_asignatura, nombre From asignaturas WHERE "\
            "id_asignatura = :asig"
            q = QtSql.QSqlQuery(self.db.database('asignaturas'))
            q.prepare(sql)
            q.bindValue(":asig", int(i))
            estado = self.ejecuto(q)
#            imp.definoEstilos('txt', 10, "Helvetica", 12)
            while estado.next():
                imp.agregoSpacer()
                imp.agregoSpacer()
                imp.agregoString("Código de Asignatura: " + str(estado.value(0)), 'txt')
                imp.agregoString("Nombre de Asignatura: " + estado.value(1), 'txt')
                imp.agregoSpacer()
        size = A4
        imp.createPageTemplate(formato, size)
        imp.cierroStory()

        imp.imprimo()
        for i in mat:
            print(i)
            '''Chequeo que al menos una de las materias sea de las carreras'''
            if int(i) < 55:
                '''Chequeo que no haya pagado la matrícula'''
                util = Utilidades()
                year = util.devuelveCiclo()

                '''Si es así, agrego el coste de matrícula al alumno'''
                '''Obtengo el valor de matricula'''
                sql = "SELECT * FROM valores"
                q = self.querys(sql)
                estado = self.ejecuto(q)
                while estado.next():
                    if q.value(1) == 'Matricula':
                        valor = q.value(2)
                        descrip = q.value(1)
                    elif q.value(1) == 'Cooperadora':
                        descripAnual = "Cooperadora Anual"
                        valorAnual = q.value(3)
                sql = "SELECT * from cuentas WHERE periodo = :per AND dni "\
                "= :dni AND detalle = :det"
                '''sql = "INSERT INTO cuentas (Alumno, periodo, asignatura, "\
                "importe, detalle, dni) VALUES (:alumno, :per, :asig, :imp, "\
                ":det, :dni)"'''

                q = self.querys(sql)
                q.bindValue(":det", descrip)
                q.bindValue(":dni", int(self.dni))
                q.bindValue(":per", year)
                estado = self.ejecuto(q)
                sql = "INSERT INTO cuentas (Alumno, periodo, asignatura, "\
                "importe, detalle, dni) VALUES (:alumno, :per, :asig, :imp, "\
                ":det, :dni)"
                if estado.size() == 0:
                    c = util.MensajeOkNo("¿Cobrar cooperadora anual?")
                    coop = c.exec_()
                    if coop == 1024:
                        q = self.querys(sql)
                        q.bindValue(":alumno", nombre)
                        q.bindValue(":per", year)
                        q.bindValue(":asig", 0)
                        q.bindValue(":imp", valorAnual)
                        q.bindValue(":det", descripAnual)
                        q.bindValue(":dni", int(self.dni))
                        estado = self.ejecuto(q)
                    q = self.querys(sql)
                    q.bindValue(":alumno", nombre)
                    q.bindValue(":per", year)
                    q.bindValue(":asig", 0)
                    q.bindValue(":imp", valor)
                    q.bindValue(":det", descrip)
                    q.bindValue(":dni", int(self.dni))
                    estado = self.ejecuto(q)
            pass
        c = self.parentWidget()
        c.alumnos()

#############################################################################

    def FOBA(self):
        '''Proceso toda la información FOBA, devuelvo una Lista con las''' \
        '''materias disponibles de FOBA para anotar al alumno'''
        '''Obtengo el total de materias FOBA'''

        sql = "SELECT * from asignaturas INNER JOIN carreras on " \
        "asignaturas.carrera = carreras.id_carrera WHERE "\
        "carreras.nombre = 'FOBA'"

        foba = QtSql.QSqlQuery(self.db.database('asignaturas'))
        foba.prepare(sql)
        foba = self.ejecuto(foba)

        sql = "SELECT * from calificaciones WHERE alumno = :dni"
        q = QtSql.QSqlQuery(self.db.database('asignaturas'))
        q.prepare(sql)
        q.bindValue(":dni", int(self.dni))
        estado = self.ejecuto(q)
        l = []
        while foba.next():
            l.append(foba.record())

        if estado.size() < 8:
            while estado.next():
                for i in l:
                    if i.value(0) == estado.value(1):
                        l.remove(i)
        else:
            total_aprobadas = 0

            while estado.next():

                for i in l:
                    if i.value(0) == estado.value(1):
                        if self.ControloNotas(estado.record()) is True:
                            total_aprobadas = total_aprobadas + 1

            if total_aprobadas == 8:
                l = True
            else:
                l = "No tiene materias disponibles para la inscripción"
        return l

##############################################################################

    def ControloNotas(self, e):

        n1 = 0
        n2 = 0
        n3 = 0
        n4 = 0

        n1 = e.value(2)

        n2 = e.value(3)

        n3 = e.value(4)

        n4 = e.value(9)
        if n4 >= 4:

            return True
        elif (n1 + n2 / 2) >= 4:

            return True
        elif (n1 + n3 / 2) >= 4:

            return True
        elif (n2 + n3 / 2) >= 4:

            return True
        else:

            return False

##############################################################################

    def ObtengoMaterias(self, c, d = 0):
        sql = "SELECT asignaturas.*, carreras.nombre as c FROM asignaturas " \
        "INNER JOIN carreras on asignaturas.carrera = carreras.id_carrera " \
        "WHERE carreras.nombre = :carrera OR carreras.nombre = :carrera2"
        q = QtSql.QSqlQuery(self.db.database('asignaturas'))
        q.prepare(sql)
        q.bindValue(":carrera", c)
        if d != 0:

            q.bindValue(":carrera2", d)
        else:
            q.bindValue(":carrera2", c)
        estado = self.ejecuto(q)
        return estado

##############################################################################

    def MateriasFoba(self, control):
        c = 'FOBA'
        if control == 0:

            datos = self.ObtengoMaterias(c)
        else:

            datos = self.FOBA()

        return datos

##############################################################################

    def ejecuto(self, q):
            estado = q.exec_()
            pipi = q.executedQuery()
            if estado is True:

                if q.isActive() is False:
                    pass
                else:
                    return q
            else:

                print((self.db.database('asignaturas').lastError()))

##############################################################################

    def CursosExtraprogramaticos(self):
        c = 'Cursos Extraprogramáticos'
        datos = self.ObtengoMaterias(c)
        self.util = Utilidades()
        mat = self.util.Convierto_a_Lista(datos)
        materias = self.Limpio_Lista(mat)
        return materias

##############################################################################

    def anotoMaterias(self, dni, materias):
        '''Preparo la sentencia para inscribir al alumno'''
        sql = "INSERT INTO calificaciones (id_asign, alumno) " \
        "VALUES " + materias

        q = QtSql.QSqlQuery(self.db.database('asignaturas'))
        q.prepare(sql)

        try:
            q.exec_()

        except:
            print(self.db.database('asignaturas').lastError())

##############################################################################

    def anotoProfTec(self):
        '''Obtengo las materias disponibles para inscribir al alumno'''
        '''Obtengo carrera del alumno'''

        sql = "SELECT carreras.nombre from carreras " \
        "INNER JOIN alumnos on alumnos.Carrera = carreras.nombre " \
        "WHERE DNI = :dni"

        q = QtSql.QSqlQuery(self.db.database('asignaturas'))
        q.prepare(sql)
        q.bindValue(":dni", self.dni)
        carrera = self.ejecuto(q)
        while carrera.next():
            carre = carrera.value(0)
        mtr = self.ObtengoMaterias(carre, 'AMBAS')
        self.util = Utilidades()
        mat = self.util.Convierto_a_Lista(mtr)
        materias = self.Limpio_Lista(mat)
        gl = self.CreoGridLista(materias,carre)
        gl.setObjectName('G' + carre)
        return gl


##############################################################################

    def Conecto_a_DB(self):
        try:
            self.db
        except:
            conn = Connection()
            conn.SetUsuario(self.usr)
            self.db = conn.CreateConnection('asignaturas')
            if self.db.database('asignaturas').isOpen():
                pass

##############################################################################

    def Limpio_Lista(self, l):
        '''Recibe una lista, busca aprobadas, correlativas, devuelve las''' \
        '''disponibles para que se anote el alumno'''

        '''Busco las materias anotadas de la carrera en las que el alumno''' \
        '''ya se encuentra anotado'''

        sql = "SELECT * FROM calificaciones WHERE alumno = :dni"
        q = QtSql.QSqlQuery(self.db.database('asignaturas'))
        q.prepare(sql)
        q.bindValue(":dni", self.dni)
        calificaciones = self.ejecuto(q)
        calif = self.util.Convierto_a_Lista(calificaciones)

        if isinstance(l, list):
            for c in calif:

                for i in l:

                    if i.value(0) == c.value(1):
                            l.remove(i)
                    else:
                        corre = self.Correlativas(i.value(3), calif)

                        if corre is False:
                            l.remove(i)


        else:
            print("No me diste una Lista")
        return l

##############################################################################

    def Correlativas(self, co, ca):
        diccio = []
        if co != "":
            co = co.split(',')
            for c in co:
                v = False
                for i in ca:

                    if c == str(i.value(1)):
                        print("La encontré")
                        cnotas = self.ControloNotas(i)
                        print("Cnotas " + str(cnotas) + " Cuatri1 " + str(i.value(2)) + " Numero de Asignatura " + str(c))
                        if cnotas is True:
                            v = True
                        else:
                            v = False
            return v
        else:
            return True


##############################################################################

    def AgregoFechaInscripcion(self):
        fecha = QDate()

        for i in self.mat:
            sql = "UPDATE calificaciones SET fecha_Inscripcion = :fecha "\
            "WHERE id_asign = :asig AND alumno = :dni"
            q = QtSql.QSqlQuery(self.db.database('asignaturas'))
            q.prepare(sql)
            q.bindValue(":fecha", fecha.currentDate())
            q.bindValue(":asig", i)
            q.bindValue(":dni", self.dni)
            calif = self.ejecuto(q)

##############################################################################

    def querys(self, sql):
        q = QtSql.QSqlQuery(self.db.database('asignaturas'))
        q.prepare(sql)
        return q