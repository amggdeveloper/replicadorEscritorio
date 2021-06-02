#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
2021
@author: amgg

Clase con los argumentos para establecer la conexión
a la base de datos correspondientes (origen o destino).
"""
#Importamos las librerias
import pymysql
import logging

class Conn(object):
   
    #Función que conecta a la base de datos correspondiente
    def Connex(self, host, user, pwd, db, port):
        try:
            #Creamos la conexión a la base de datos    
            self.db=pymysql.connect(user=user, passwd=pwd, host=host, db=db, port=port)  
            self.cursor=self.db.cursor()
            #Registramos el evento en el log       
            logging.info(f'Conexión establecida.')
            return db 
        
        #Capturamos las excepciones         
        except Exception as err:
            self.error="Error: %s" %(err)
            logging.error('Error de conexión')
        except:
            self.error="Error desconocido" 
            logging.error('Error desconocido')
        return False       

    #Cursor
    def getData(self,sql):
        try:
            self.cursor.execute(sql)           
            datos=self.cursor.fetchall()                        
                                                               
        except Exception as err:
            raise  
          
        return datos