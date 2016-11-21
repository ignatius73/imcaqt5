import sys, logging, base64
from PyQt5 import QtSql
from utilidades import *
from login import *



class Connection(QtSql.QSqlDatabase):

    def __init__(self):
        super(Connection, self).__init__()
        #Seteo los datos de conexión
        logging.basicConfig(filename='logs/debug.log',level=logging.DEBUG)
        logging.warning("Atención")


    def SetUsuario(self, usr):
        self.usr = usr



    def GetUsuario(self):
        #  Envio tupla usuario
        return self.usr

    def CreateConnection(self, nombre = None):
        db = QtSql.QSqlDatabase.addDatabase('QMYSQL', nombre)
        db.setHostName('127.0.0.1')
        db.setDatabaseName('imca')
        db.setUserName(self.usr[0])

        db.setPassword(base64.b64decode(self.usr[1]).decode("utf-8", "ignore"))

        if db.open() is True:
            print("base de datos conectada")
            return db
        else:
            db.close()
            logging.warning(db.lastError())
            return False


    def GetConnection(self):
            return self.db

    def ConsultoDNI(self, dni,db):
        '''Consulta a la DB si el alumno ya está inscripto'''

        sql = "SELECT * from alumnos WHERE DNI = :dni"

        if db.database('principal').isOpen() is True:

            q = QtSql.QSqlQuery(db)
            q.prepare(sql)
            q.bindValue(":dni", int(dni))
            estado = q.exec_()
            pipi = q.executedQuery()

            if estado:
                if q.isActive() is False:
                    pass
                else:
                    if q.size() > 0:

                        return True
                    else:
                        return False

            else:


                logging.warning((db.lastError()))
        else:
            return False

    def conecto(self, usuario = None):
        # Chequeo si los datos del usuario existen
        try:
            self.usr
        except:

            self.SetUsuario(self)
            try:
                self.db
            except:
                self.db = self.CreateConnection(self.usr[0], self.usr[1])
                return self.db

    def conecto_a_DB(self, usr, base):
        self.SetUsuario(usr)
        self.dba = self.CreateConnection(base)
        if self.dba.database(base).isOpen():
            logging.warning("Conexión exitosa a " + base)
        return self.dba

##############################################################################

    def ejecuto(self, q, db):
            estado = q.exec_()
            pipi = q.executedQuery()
            if estado is True:

                if q.isActive() is False:
                    print("La consulta no está activa")
                else:
                    return q
            else:
                util = Utilidades()
                g = util.Mensaje("Ocurrió un error al insertar el alumno. "\
                "Vuelve a intentarlo. Si el problema persiste comunicate con "\
                "el Administrador" + str(self.dba.database(db).lastError()))
                g.exec_()
                return False