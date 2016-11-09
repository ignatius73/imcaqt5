import sys, re, datetime
from PyQt5 import QtCore, QtGui, QtSql, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget
from PyQt5.QtCore import QDate, QTime
from PyQt5.QtCore import Qt



class Utilidades():

    def __init__(self):
        super(Utilidades, self).__init__()

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

    def Confirmar(self, t):
        '''Muestra Cuadro de dialogo para la confirmacion. Recibe el texto a mostrar'''
        '''Creo el Cuadro de dialogo'''
        w = QtWidgets.QWidget()
        v = QMessageBox.question(w, "Atención", t, QMessageBox.Ok | QMessageBox.Cancel)
        w.show()
        return v

##############################################################################

    def Convierto_a_Lista(self, obj):
        '''Recibe un QtSqlQuery y devuelve una Lista'''
        if isinstance(obj, QtSql.QSqlQuery):
            l = []
            while obj.next():
                l.append(obj.record())
            return l
        else:
            return "No me diste un Query"

##############################################################################

    def Convierto_a_tabla(self, obj):
        '''Recibe un QtSqlQuery y devuelve una Lista de listas'''
        if isinstance(obj, QtSql.QSqlQuery):
            l = []
            a = []

            while obj.next():
                l.append(obj.record())
            for i in l:
                b = []
                for r in range(i.count()):
                    b.append(i.value(r))
                a.append(b)
                b = None

            return a
        else:
            return "No me diste un Query"

##############################################################################

    def ejecuto(self, q, db):
            estado = q.exec_()
            pipi = q.executedQuery()
            if estado is True:
                print("estado true")
                if q.isActive() is False:
                    print("La consulta no está activa")
                else:
                    return q
            else:
                print(pipi)
                print((self.db.database(db).lastError()))

##############################################################################

    def Pruebo_Tipo(self, v):
        try:
            v = float(v)
            return v
        except:
            return False

#################################################################

    def Mensaje(self, msg):
        ventana = QtWidgets.QMessageBox()
        ventana.setText(msg)
        ventana.setIcon(QMessageBox.Information)
        ventana.setStandardButtons(QMessageBox.Ok)
        return ventana

#################################################################

    def CreoTabla(self, q, campos):
        '''Recibe una query'''
#        self.setWindowTitle("Módulo de Calificaciones")
#        self.frm = QtWidgets.QFrame()
#        self.layout = QtWidgets.QGridLayout()
#        self.setLayout(self.layout)
#        self.sb = QtWidgets.QScrollArea()
#        self.et = QtWidgets.QLabel()
        self.table = QtWidgets.QTableWidget()
#        self.sb.setWidget(self.frm)
#        self.layout.addWidget(self.table)
        self.table.setColumnCount(len(campos))
        self.table.setHorizontalHeaderLabels(campos)
        row = 0
        col = 0
        while q.next():
            self.table.insertRow(row)
            for i in campos:
                self.table.setItem(row, col, QtWidgets.QTableWidgetItem(str(q.value(col))))
                self.table.resizeColumnToContents(col)
                col = col + 1
            self.table.resizeRowToContents(row)

            row = row + 1
            col = 0

        '''Divido el ancho por la cantidad de filas'''

        return self.table

##############################################################################

    def convierte_Fechas(self, fe):
        nueva = datetime.datetime.strptime(fe,"%d/%m/%Y").date().strftime("%Y-%m-%d")
        return nueva

##############################################################################

    def meses(self):
        '''Devuelve un diccionario con los meses en español'''
        meses = {1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'}
        return meses

##############################################################################

    def devuelvePeriodo(self):
        periodo = QDate().currentDate()
        mes = periodo.month()
        anio = periodo.year()
        util = Utilidades()
        meses = util.meses()
        mes = meses[mes]
        mes = mes + " " + str(anio)
        return mes

##############################################################################

    def limpia(self, t):
        '''Recibe un QLineEdit, los limpia'''
        t.setText('')

##############################################################################

    def MensajeOkNo(self, msg):
        ventana = QtWidgets.QMessageBox()
        ventana.setText(msg)
        ventana.setIcon(QMessageBox.Information)
        ventana.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        return ventana

##############################################################################

    def dicciolista(self, diccio):

        list = []
        valores = diccio.values()
        for i in valores:

            list.append(i)

        return list

##############################################################################

    def invDict(self, diccio):

        inv_diccio = {v: k for k, v in diccio.items()}
        return inv_diccio

##############################################################################

    def estiloTablas(self,t, r):

        appStyle="""
                QTableView
                {
                    background-color: grey;
                    gridline-color:white;
                    color: black;
                }
                QTableView::item
                {
                    color: white;
                }
                QTableView::item:hover
                {
                    color: black;
                    background: #ffaa00;
                }
                QTableView::item:focus
                {
                    color: black;
                    background: #0063cd;
                }
                """
        r.setStyleSheet(appStyle)
