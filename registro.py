import sys
from PyQt5 import QtCore, QtSql, uic, QtWidgets, QtPrintSupport
from conn import *
from utilidades import *
from asignaturas import *
from PyQt5.QtCore import QDate, QTime
from PyQt5.QtCore import Qt


class Registro():

    def __init__(self, usr):
        super(Registro, self).__init__()
        self.usr = usr
        self.conn = Connection()
        self.db = self.conn.conecto_a_DB(self.usr, 'registros')

##############################################################################

##############################################################################

    def registra(self):
        '''Obtengo último registro de ingreso'''
        sql = "SELECT * FROM registros ORDER BY id DESC LIMIT 1"
        q = QtSql.QSqlQuery(self.db.database('registros'))
        q.prepare(sql)
        ej = self.conn.ejecuto(q,'registros')

        if ej != False:
            if q.size() > 0:
                while q.next():
                    '''Obtengo la fecha del ultimo registro'''
                    ant = q.value(1)
                hoy = QDate().currentDate()
                sql = "INSERT INTO registros (fecha, hora, user) VALUES"\
                " (CURDATE(), CURTIME(), :usr)"
                q.prepare(sql)
                q.bindValue(":usr", self.usr[0])

                if hoy.month() != ant.month():
                    self.month = hoy.month()
                    ej = self.conn.ejecuto(q, 'registros')
                    meses = {1:'a',2:'a',3:'b',4:'b',5:'b',6:'b', 7:'b',
                             8:'b',9:'b',10:'b',11:'b',12:'b'}
                    if meses[hoy.month()] == 'a':
                        '''No hace nada ya que no tiene cargo'''
                        print("No paga cooperadora")
                    else:
                        self.costea()
                        print("Paga cooperadora y cursos")
            else:
                sql = "INSERT INTO registros (fecha, hora, user) VALUES"\
                " (CURDATE(), CURTIME(), :usr)"
                q.prepare(sql)
                q.bindValue(":usr", self.usr[0])
                ej = self.conn.ejecuto(q, 'registros')



        else:
            self.costea()
##############################################################################

    def costea(self):
        '''Agrega costos por cooperadora y cursos'''
        #  Busca el listado de alumnos inscriptos
        util = Utilidades()
        mes = util.devuelvePeriodo()
        coop = None
        dniAnt = None
        sql = "SELECT calificaciones.id_asign, calificaciones.alumno, "\
        "calificaciones.fecha_inscripcion, asignaturas.nombre, "\
        "asignaturas.duracion, asignaturas.valor, alumnos.Nombre as Nombre_Alumno from calificaciones "\
        "INNER JOIN asignaturas ON calificaciones.id_asign = "\
        "asignaturas.id_asignatura INNER JOIN alumnos ON calificaciones.alumno"\
        " = alumnos.DNI"
        q = QtSql.QSqlQuery(self.db.database('registros'))
        q.prepare(sql)
        ej = self.conn.ejecuto(q, 'registros')
        print(q.executedQuery())
        print(q.size())
        sql = "INSERT INTO cuentas (Alumno, periodo, asignatura, "\
        "importe, detalle, dni, docente) VALUES (:alumno, :per, :asig, :imp, "\
        ":det, :dni, :doc)"
        qu = QtSql.QSqlQuery(self.db.database('registros'))
        qu.prepare(sql)
        if q.size() > 0:
            while q.next():

                print("DNI " + str(q.value(1)))
                qu.bindValue(":per", mes)
                qu.bindValue(":asig", q.value(0))
                qu.bindValue(":imp", q.value(5))
                qu.bindValue(":dni", q.value(1))
                qu.bindValue(":alumno", q.value(6))
                if q.value(0) > 55:
                    qu.bindValue(":doc", 1)
                    '''Controlo cantidad de cuotas pagas de la asignatura'''
                    cant = self.cantCuotas(q.value(0), q.value(1))
                    '''Busco en cuentas cuantas cuotas se pagaron de la'''
                    ''' asignatura'''
                    if cant < q.value(4):
                        qu.bindValue(":det", q.value(3))
                        self.conn.ejecuto(qu,'registros')
                        print(qu.executedQuery())
                else:
                    dni = q.value(1)
                    print(type(dni))
                    anual = self.coopAnual(dni)
                    print(type(anual))
                    print(anual)
                    if anual != True:
                        self.valores("Cooperadora")
                        qu.bindValue(":doc", 0)
                        qu.bindValue(":asig", 0)
                        if coop == None:
                            dniAnt = q.value(1)
                            coop = True
                            qu.bindValue(":det", "Cooperadora")
                            qu.bindValue(":imp", self.valor)
                            self.conn.ejecuto(qu,'registros')
                        elif dniAnt != q.value(1):
                            dniAnt = q.value(1)
                            qu.bindValue(":det", "Cooperadora")
                            qu.bindValue(":imp", self.valor)
                            self.conn.ejecuto(qu,'registros')


##############################################################################

    def cantCuotas(self, mat, dni):
        print("Cant cuotas " + str(mat))
        print("Cant cuotas " + str(dni))
        sql = "SELECT Count(*) from cuentas WHERE asignatura = :mat AND "\
              "dni = :dni"
        que = QtSql.QSqlQuery(self.db.database('registros'))
        que.prepare(sql)
        print(type(mat))
        print(type(dni))
        que.bindValue(":mat" , mat)
        que.bindValue(":dni", dni)
        ej1 = self.conn.ejecuto(que, 'registros')
        print(que.executedQuery())
        if ej1 != False:
            print("La query es correcta")
            while que.next():
                print(que.value(0))
                cant = que.value(0)
            return cant
        else:
            cant = 0
            return cant

##############################################################################

    def valores(self, mov):
        print("entro a valores")
        '''Obtengo los valores y la descripción del tipo de movimiento'''
        sql = "SELECT * from valores WHERE descripcion = :desc"
        que = QtSql.QSqlQuery(self.db.database('registros'))
        que.prepare(sql)
        que.bindValue(":desc" , mov)

        ej1 = self.conn.ejecuto(que, 'registros')
        print(que.executedQuery())
        if ej1 != False:
            print("La query es correcta")
            while que.next():
                self.desc = que.value(1)
                self.valor = que.value(2)
                self.anual = que.value(3)

##############################################################################

    def coopAnual(self, dni):
        print("entro a anual")
        '''Busco si el alumno decidió pagar la cooperadora anual con desc'''
        util = Utilidades()
        ciclo = util.devuelveCiclo()
        sql = "SELECT * from cuentas WHERE detalle = 'Cooperadora Anual' AND "\
        "periodo = :periodo AND dni = :dni"
        print(sql)
        print(ciclo)
        print(dni)
        que = QtSql.QSqlQuery(self.db.database('registros'))
        que.prepare(sql)
        que.bindValue(":periodo" , ciclo)
        que.bindValue(":dni" , dni)
        ej1 = self.conn.ejecuto(que, 'registros')
        print(que.executedQuery())
        if ej1 != False:
            print("La query es correcta")
            if que.size() > 0:
                print("hay al menos un pago de cooperadora anual para el alumno")
                print(dni)
                return True
            else:
                return False
        else:
            return False
