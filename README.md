# agencia_back
Configuración

A continuación se explicarán los pasos a seguir para hacer funcionar el proyecto.

## Base de datos

La base de datos utilizado para este proyecto es pgAdmin de PostgreSQL para almacenar la información. Para descargarlo dirigese a la página oficial https://www.pgadmin.org/download/.

Para que funciona el proyecto se recomienda poner la misma contraseña que se encuentra en el modulo c:\<carpeta_proyecto>\agencia-back-master\Viaje_API settings.py.

Despues de terminar con las configuraciones correspondientes, crea una nueva base de datos con el nombre AgenciaViaje. 

## Configuración del backend

El primer paso es instalar Python 3.10.5 desde la página https://www.python.org/downloads/release/python-3105/, se tiene que descargar el archivo que corresponda a las especificaciones de su sistema. Recuerde marcar la casilla de agregar python al PATH de su sistema.

Una vez que el proyecto se haya descargado y se haya copiado el contenido a una carpeta de proyecto. Navegar al directorio de instalación donde se haya guardado: cd c:\<carpeta_proyecto>\agencia-back-master\Viaje_API y empezar a instalar las dependencias.
 
 ## Nota: 
 
    1- Recuerda que el usuario debe tener permiso de administrador en las carpetas donde se guardo el proyecto
    2- Que este permitido la ejecución de script en su maquina.

## Para la instalación de las librerias:

    1- Abre una terminal 
    2- Dirigirse al directorio donde se encuentra el archivo "requerimientos.txt" (cd c:\<carpeta_proyecto>\agencia-back-master\Viaje_API).
    3- Después ejecutar el comando pip install -r requerimientos.txt en la terminal para empezar a descargar las dependencias del proyecto.
    4- Una vez terminado, entra al directorio cd c:\<carpeta_proyecto>\agencia-back-master\ y ejecuta los comandos siguientes para crear un ambiente virtual
        - pip install virutalenv para instalar
        - virtualenv env para crear el ambiente
        - navegar desde la teminal a cd c:\<carpeta_proyecto>\agencia-back-master\env\Scripts
        - luego escriba .\activate para activar el ambiente
     A este punto le saldra en la terminal "(env) c:\<carpeta_proyecto>\agencia-back-master\env\Scripts"
        -regresa a esta dirección desde la terminal "cd c:\<carpeta_proyecto>\agencia-back-master\Viaje_API"
     y ejecuta "pip install -r requerimientos.txt" para instalar los requerimientos  luego ejecuta
     
    1- python manage.py makemigrations
    2- python manage.py migrate
    3- python manage.py runserver
    
    Si en este punto le saldra algun error, procederé a ejecutar los comandos siguientes
     -pip install django==2.2
     -pip install django-admin
     -pip install django-cors-headers
     -pip install djangorestframework
     -pip install pyodbc
     -python manage.py migrate
   y por último para correr el proyecto escriba python manage.py runserver.

## Configuración front end
 
 Una vez que se descarga y se copia el contenido a una carpeta de proyecto, ejecuta el siguiente comando en una terminal donde se encuentra el proyecto
 "cd c:\<carpeta_proyecto>\agencia-front-master" para instalar las librerias
   - npm install
   - npm run server
 
