#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
2021
@author: amgg

Clase encargada de recoger los datos en formato JSON de la
cola creada con RabbitMQ e introducirlos en la base de datos
destino.

"""
#Importamos las librerias
from conn import*
import logging
import json
import pika

class Destino():
    
    #Constructor
    def __init__(self):
        print(' ')    
         
    #Función que recibe los datos json de la cola creada en RabbitMQ
    def recibirCola(self):
        #Establecemos la conexión con RabbitMQ
        con=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        ch=con.channel()
        
        #Declaramos la cola
        cola=ch.queue_declare(queue='replicador')
               
        #Función de recepción
        def reception(ch,method,properties,body):            
            datos=json.loads(body)
            d.introducirDatosBD(datos)
            
        #Enganchamos al callback
        ch.basic_consume(queue='replicador',on_message_callback=reception, auto_ack=True)
        
        #Mensaje de salida de recepcion de datos
        print('recibiendo datos de la cola')
        logging.info('recibiendo datos de la cola')    
        
        #Cerrar conexión
        ch.start_consuming()       

    #Función que introduce los datos recogidos en la BD destino
    def introducirDatosBD(self,datas):
        #LLamamos al objeto conexión
        conn=Conn()
        con=conn.Connex('localhost','chuguisapp','daw2021','chuguisappcopia',3306)
        cursor=conn.db.cursor()
        
        for datos in datas:
            cod=datos[0]
            nombre=datos[1]
            email=datos[2]
            contra=datos[3]
            contra2=datos[4]
            picture=datos[5]           

            codigo=d.repetido(cod)
            
            if codigo==None:
                cursor.execute('INSERT INTO users (name,mail,pass,pass2, picture) VALUES (%s,%s,%s,%s,%s)',(nombre,email,contra,contra2,picture))
                conn.db.commit()
            elif cod == codigo[0]:                 
                cursor.execute('UPDATE users SET name=%s,mail=%s,pass=%s,pass2=%s,picture=%s WHERE id=%s',(nombre,email,contra,contra2,picture,cod))
                conn.db.commit()                     
            else:
                print('---')   
        conn.db.close()  
        
    #Función que comprueba que no se introduzca ningun dato repetido
    def repetido(self, codigo):
        #LLamamos al objeto conexión
        conn=Conn()
        con=conn.Connex('localhost','chuguisapp','daw2021','chuguisappcopia',3306)
        cursor=conn.db.cursor()
        #Creamos la consulta a la base de datos correspondiente
        sql='SELECT * FROM users WHERE id= %s'
        cursor.execute(sql,codigo)
        datos=cursor.fetchone()                  
        return datos
    
d=Destino()
d.recibirCola()
    
    
