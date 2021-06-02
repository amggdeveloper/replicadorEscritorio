#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
2021
@author: amgg

Clase encargada de recoger los datos de la base de datos
origen e introducirlos en formato JSON e introducirlos en
la cola usando RabbitMQ.

"""
#Importamos las librerias
from conn import*
import logging
import json
import pika
from random import randint
import time

class Origen():
    
    #Constructor
    def __init__(self):
        logging.info('Empieza Origen')           
        
    #Función que recoge los datos de la BD de origen
    def recogerDatos(self):
        #Creamos un objeto para la conexión 
        conn=Conn()
        con=conn.Connex('localhost','chuguisapp','daw2021','chuguisapp',3306)
        
        #Creamos la consulta a la BD 
        sql='SELECT id,name,mail,pass,pass2,picture FROM users'
        
        #Metemos en una tupla los datos                  
        info=conn.getData(sql)        
        
        #Pasamos los datos a formato json
        datosJson=json.dumps(info,indent=6)
        return datosJson
    
    #Función para craer la cola con RabbitMQ
    def crearCola(self):
        #Establecemos la conexión con RabbitMQ
        con=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        ch=con.channel()
        
        #Declaramos la cola
        ch.queue_declare(queue='replicador')
        
        #Bucle infinito
        while True:
            #Tiempo aleatorio antes de volver a lanzar el mensaje
            time.sleep(randint(1,2))
            #Recogemos los datos json obtenidos de la BD origen
            dtJson=o.recogerDatos()
        
            #Introducimos los datos en la cola
            ch.basic_publish(exchange='', routing_key='replicador',body=dtJson)
        
            #Cerramos la conexión
            #con.close()
        
o=Origen()
o.crearCola()  