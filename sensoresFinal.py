__author__ = 'Elkin'

from datetime import datetime  # API del Tiempo
import urllib.request  # API de conexion al web Service
import urllib.parse  # API Parseo Conexion
import requests  # API de conexion al web Service
import json  # API manejo JSON
import os

os.system("sudo python /home/pi/Documents/urbaneyes/sensores.py")
archivotemperatura = open("/home/pi/Documents/urbaneyes/temperatura.kin")
temperatura = archivotemperatura.read()
archivotemperatura.close()
archivohumedad = open("/home/pi/Documents/urbaneyes/humedad.kin")
humedad = archivohumedad.read()
archivohumedad.close()

#url del web service
url = 'http://181.118.150.147'
url_Check = url+'/sensor/list/'
url_Add = url+'/sensor/create/'

#manejo del tiempo
tiempo = datetime.now()
format = "%d-%m-%Y_%H:%M:%S"
date_time = tiempo.strftime(format)
#date_time = "00-00-00_00:00:00"
###date_time = "23-08-015_13:39:30"
#print (date_time)

#parametros necesarios para agregar la informacion del web service
value_T = temperatura
description_T = "Sensor4"
variable_Id_T = "4"

value_H = humedad
description_H = "Sensor5"
variable_Id_H = "5"


description_H = "Sensor5"
variable_Id_H = "5"

# Obtenemos latitud y longitu
x = urllib.request.urlopen('http://www.cual-es-mi-ip.net/geolocalizar-ip-mapa')
dato = str(x.read())
indice  = dato.index("data-latitud")
inicio = indice + 14;
fin = inicio + 8
latitude = dato[inicio:fin]

indice  = dato.index("data-longitud")
inicio = indice + 15;
fin = inicio + 8
longitude = dato[inicio:fin]


# esta funcion comprueba si el web service tiene habilitado el sensor para poder $
def check(url, id):
    try:
        values = ""
        data = urllib.parse.urlencode(values)
        data = data.encode('utf-8')
        req = urllib.request.Request(url, data)
        resp = urllib.request.urlopen(req)
        respData = resp.read()
        writeFile(respData, True)
        return check_State(str(respData), id)
    except Exception as e:
        error = "Error Solicitud de Comprobacion" + str(e)
        writeFile(error, False)
        return False

# DESHABILITADA... esta funcion envia los valores hacia el web service para agreg$
def add_Record(url, parameters):
    try:
        data = urllib.parse.urlencode(parameters)
        data = data.encode('utf-8')
        req = urllib.request.Request(url, data)
        resp = urllib.request.urlopen(req)
        print ("Datos Agregados")
        respData = resp.read()
        writeFile(respData, True)
        return respData
    except Exception as e:
        error = "Error al agregar informacion del Sensor " + str(e)
        writeFile(error, False)
       error = "Error al agregar informacion del Sensor " + str(e)
        writeFile(error, False)


# Esta funcion envia los valores hacia el web service para agregarlos
def add_info(url, value, latitude, longitude, description, date_time, variable_id$
    try:
        #payload = "value="+value+"&latitude="+latitude+"&longitude="+longitude+"$
        #cabecera = "application/x-www-form-urlencoded"
        headers = {'content-type': "application/x-www-form-urlencoded" }
        payload = "value="+value+"&latitude="+latitude+"&longitude="+longitude+"&$
        writeFile(payload, True)
        print (payload)
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)
    except Exception as e:
        error = "Error al agregar informacion del Sensor " + str(e)
        writeFile(error, False)

# esta funcion comprueba el estado si es True o False
def check_State(answer, id):
    info = answer.lstrip("b,'")
    info = info.rstrip("'")
    dato = json.loads(info)
    valor = (dato[id]['enable'])
    #print(valor)
    return (valor)

# en esta funcion creamos 2 (reportes y errores) archivos y agregamos reporte de $
def writeFile(respData, type):
    if type == True:
        saveFile = open('/home/pi/Documents/urbaneyes/registros/registro.rgt', 'a$
        saveFile.write(str(date_time + "\n" + str(respData)+"\n \n" ))
        saveFile.close()
    elif type == False:
        error = date_time + "\n" + str(respData) + "\n  \n"
        errorFile = open('/home/pi/Documents/urbaneyes/registros/error.rgt', 'a')
        errorFile.write(str(error))
       error = "Error al agregar informacion del Sensor " + str(e)
        writeFile(error, False)


# Esta funcion envia los valores hacia el web service para agregarlos
def add_info(url, value, latitude, longitude, description, date_time, variable_id$
    try:
        #payload = "value="+value+"&latitude="+latitude+"&longitude="+longitude+"$
        #cabecera = "application/x-www-form-urlencoded"
        headers = {'content-type': "application/x-www-form-urlencoded" }
        payload = "value="+value+"&latitude="+latitude+"&longitude="+longitude+"&$
        writeFile(payload, True)
        print (payload)
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)
    except Exception as e:
        error = "Error al agregar informacion del Sensor " + str(e)
        writeFile(error, False)

# esta funcion comprueba el estado si es True o False
def check_State(answer, id):
    info = answer.lstrip("b,'")
    info = info.rstrip("'")
    dato = json.loads(info)
    valor = (dato[id]['enable'])
    #print(valor)
    return (valor)

# en esta funcion creamos 2 (reportes y errores) archivos y agregamos reporte de $
def writeFile(respData, type):
    if type == True:
        saveFile = open('/home/pi/Documents/urbaneyes/registros/registro.rgt', 'a$
        saveFile.write(str(date_time + "\n" + str(respData)+"\n \n" ))
        saveFile.close()
    elif type == False:
        error = date_time + "\n" + str(respData) + "\n  \n"
        errorFile = open('/home/pi/Documents/urbaneyes/registros/error.rgt', 'a')
        errorFile.write(str(error))

      errorFile = open('/home/pi/Documents/urbaneyes/registros/error.rgt', 'a')
        errorFile.write(str(error))
        print(error)
        errorFile.close()

# en esta funcion inicia el proceso de comprobacion y envio de informacion
def process(url_Check, id, url_Add, value, latitude, longitude, description, date$
    if check(url_Check, id) == True:
        #add_Record(url_Add, parameters)
        add_info(url_Add, value, latitude, longitude, description, date_time, var$
        return (True)
    else:
        text = "Sensor " + id + " Inhabilitado"
        writeFile(text, "no")
        print ("Sensor Inhabilitado" + id)

# inicializamos el proceso
def start(url_Check, id, url_Add, value, latitude, longitude, description, date_t$
    process(url_Check, id, url_Add, value, latitude, longitude, description, date$

start(url_Check, 1, url_Add, value_T, latitude, longitude, description_T, date_ti$
start(url_Check, 2, url_Add, value_H, latitude, longitude, description_H, date_ti$




