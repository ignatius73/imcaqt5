class Numeros():

    def __init__(self):
        super(Numeros, self).__init__()

##############################################################################

    def numero_to_letras(self, numero):
        indicador = [("",""),("Mil","Mil"),("Millon","Millones"),("Mil","Mil"),("Billon","Billones")]
        entero = int(numero)
        decimal = int(round((numero - entero)*100))

        print ('decimal : ' + str(decimal))

        contador = 0

        numero_letras = ""

        while entero >0:

            a = entero % 1000

            if contador == 0:

                en_letras = convierte_cifra(a,1).strip()
            else :
                en_letras = convierte_cifra(a,0).strip()
            if a==0:
                numero_letras = en_letras+" "+numero_letras
            elif a==1:
                if contador in (1,3):
                    numero_letras = indicador[contador][0]+" "+numero_letras
                else:
                    numero_letras = en_letras+" "+indicador[contador][0]+" "+numero_letras
            else:
                numero_letras = en_letras+" "+indicador[contador][1]+" "+numero_letras
                numero_letras = numero_letras.strip()
                contador = contador + 1
                entero = int(entero / 1000)
                numero_letras = numero_letras+" con " + str(decimal) +"/100"
        print ('numero: ' + str(numero))
        print (numero_letras)
        return numero_letras

##############################################################################

def convierte_cifra(numero,sw):
    print('numero' + str(numero))
    print('sw' + str(sw))

    lista_centana = ["",                                             ("Cien","Ciento"),"Doscientos","Trescientos","Cuatrocientos","Quinientos","Seiscientos","Setecientos","Ochocientos","Novecientos"]

    lista_decena = ["",("Diez","Once","Doce","Trece","Catorce","Quince","Dieciseis","Diecisiete","Dieciocho","Diecinueve"),("Veinte","Veinti"),("Treinta","Treinta y "),("Cuarenta" , "Cuarenta y "),("Cincuenta" , "Cincuenta y "),("Sesenta" , "Sesenta y "),    ("Setenta" , "Setenta y "),("Ochenta" , "Ochenta y "),("Noventa" , "Noventa y ")]

    lista_unidad = ["",("Un" , "Uno"),"Dos","Tres","Cuatro","Cinco","Seis","Siete","Ocho","Nueve"]

    centena = int (numero / 100)

    decena = int((numero -(centena * 100))/10)

    unidad = int(numero - (centena * 100 + decena * 10))

    #print "centena: ",centena, "decena: ",decena,'unidad: ',unidad



    texto_centena = ""

    texto_decena = ""

    texto_unidad = ""



    #Validad las centenas

    texto_centena = lista_centana[centena]

    if centena == 1:

        if (decena + unidad)!=0:
            texto_centena = texto_centena[1]
        else:
            texto_centena = texto_centena[0]



    #Valida las decenas

    texto_decena = lista_decena[decena]
    if decena == 1 :
        texto_decena = texto_decena[unidad]
    elif decena > 1 :
        if unidad != 0 :
            texto_decena = texto_decena[1]
        else:
            texto_decena = texto_decena[0]

    #Validar las unidades

    #print "texto_unidad: ",texto_unidad

    if decena != 1:

        texto_unidad = lista_unidad[unidad]
        if unidad == 1:
            texto_unidad = texto_unidad[sw]

    return "%s %s %s" %(texto_centena,texto_decena,texto_unidad)