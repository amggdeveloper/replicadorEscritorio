replicador
==========

Script realizado para replicar bases de datos mysql.
Los datos se recuperan de la BD origen y se introducen en 
una cola con RabbitMQ en formato Json.
Posteriormente recuperamos esos datos json de la cola y los
introducimos en la BD destino.

Casos de Uso
============

* MySQL a Mysql replicación base de datos automatico

Documentación
=============

* RabbitMQ, usuario=guest, contraseña=guest

Installation
============

* Instalación de Python necesaria
* Librerias necesarias: 
    - PyQt5
    - Subprocess
    - Signal 
    - Pika
    - Json
* Las librerias se instalan:
    - Abrimos una terminal
    - pip install (libreria correspondiente) 

Funcionamiento
==============
* Inicializamos la Interfaz Gráfica dando doble click sobre el fichero interfazReplicador.py
* Dicha Interfaz está compuesta por cuatro botones:
    - boton Origen: Inicializa el subproceso que produce (recoge) los datos de la base de datos origen, 
                    los convierte a formato Json, crea la cola con el nombre prefijado y sube a la cola 
                    en RabbitMQ los datos de la base de datos.
    - boton Destino: Inicializa el subproceso que consume (inserta) los datos, recoge los datos en formato Json
                     y los inserta en la base de datos de destino.   
    - boton Terminar: Finaliza los dos subprocesos abiertos.
    - boton Limpiar Consola: Deja en blanco la consola de información.

* En el caso que no se pulse el boton de terminar antes de cerrar la Interfaz, los dos subprocesos se quedarán 
  en segundo plano trabajando. Si se pulsara varias veces sobre botón origen o destino, abrirá subprocesos nuevos, 
  teniendo varios subprocesos de cada uno.                               

Tests
=====

* version 1.0
* version python 3.9

Licencia
========
Copyright 2021 amgg

