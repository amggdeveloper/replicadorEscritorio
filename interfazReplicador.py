#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
2021
@author: amgg

Clase con los argumentos para establecer la conexión
a la base de datos correspondientes (origen o destino).
"""
from PyQt5 import QtWidgets, uic, QtGui, QtCore
import sys
import subprocess
from subprocess import *
from conn import *
import time
import os
import signal

class ReplicadorEscritorio(QtWidgets.QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(ReplicadorEscritorio,self).__init__(*args, **kwargs)

        #Cargamos el ui
        fileh=QtCore.QFile('interfaz.ui')
        fileh.open(QtCore.QFile.ReadOnly)
        win=uic.loadUi('replicador.ui',self)
        win.setWindowTitle('Replicador BD')
        fileh.close()
        
        #Acciones de los botones
        self.btnOrigen.clicked.connect(self.funcionOrigen)
        self.btnDestino.clicked.connect(self.funcionDestino)
        self.btnCerrar.clicked.connect(self.cerrar)
        self.btnLimpiar.clicked.connect(self.limpiar)

    #Función que se encarga de llevar a cabo la acción del botón origen
    def funcionOrigen(self):
        hora=time.strftime("%H:%M:%S")
        self.consola('%s---) Has pulsado Origen' %hora)  
        try:        
            self.origen=subprocess.Popen(['python','origen.py'],shell=True) 
           
        except subprocess.CalledProcessError as err:
            self.consola(err)                      
        
    
    #Función que se encarga de llevar a cabo la acción del botón destino
    def funcionDestino(self):
        hora=time.strftime("%H:%M:%S")
        self.consola('%s---) Has pulsado Destino' %hora) 
        try:        
            self.destino=subprocess.Popen(['python','destino.py'],shell=True)               
        except subprocess.CalledProcessError as err:
            self.consola(err)                      
        
    
    #Función que cierra los subprocesos
    def cerrar(self):
        hora=time.strftime("%H:%M:%S")
        self.consola('%s---) Has parado el replicador' %hora) 
        os.kill(self.origen.pid,signal.CTRL_BREAK_EVENT)
        os.kill(self.destino.pid,signal.CTRL_BREAK_EVENT)
        
    #Función que añade al cuadro de texto el proceso
    def consola(self,m):
        self.txtSalida.appendPlainText(m)    
        
    #Función para borrar la información de la consola
    def limpiar(self):
        self.txtSalida.clear()        
            
if __name__=='__main__':        
    app=QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('logo.ico'))
    window=ReplicadorEscritorio() 
    window.show()        
    sys.exit(app.exec_())


