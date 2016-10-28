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
                    ej = self.conn.ejecuto(q, 'registros')

                meses = {1:'a',2:'a',3:'b',4:'b',5:'b',6:'b', 7:'b',
                         8:'b',9:'b',10:'b',11:'b',12:'a'}
                if meses[hoy.month()] == 'a':
                    print("No paga cooperadora")
                else:
                    print("Paga cooperadora y cursos")
            else:
                sql = "INSERT INTO registros (fecha, hora, user) VALUES"\
                " (CURDATE(), CURTIME(), :usr)"
                q.prepare(sql)
                q.bindValue(":usr", self.usr[0])
                ej = self.conn.ejecuto(q, 'registros')



        else:
            print("vacio")

