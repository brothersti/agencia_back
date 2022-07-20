# agencia_back
Configuración
A continuación se explicarán los pasos a seguir para hacer funcionar el proyecto.

El primer paso es instalar Python 3.10.5 desde la página https://www.python.org/downloads/release/python-3105/, se tiene que descargar el archivo que corresponda a las especificaciones de su sistema.
Recuerde marcar la casilla de agregar python al PATH de su sistema.

Para la instalación de las librerias de python:
    1- Abre un terminal 
    2- Dirigirse al directorio donde se encuentra el archivo "requerimientos.txt". Esto está ubicado en la carpeta raiz del proyecto.
    3- Instalar las librerías necesarias utilizando pip install -r requerimientos.txt en el terminal.

Base de datos
La base de datos utilizado para este proyecto es SQL Server para almacenar la información. Para descargar Server dirigese a la página oficial https://www.microsoft.com/es-mx/sql-server/sql-server-downloads
y seleccionar la version Express. Despues crea una nueva base de datos con el nombre AgenciaViaje. 

Una vez terminado se debe configurar su usuario en el archivo settings.py en el proyecto de Agencia_Back/Viaje_API
En este archivo(settings.py) en el apartado DATABASES en HOST ponga el nombre de su servidor. Despues ubicáse en la carpeta Viaje_API desde la terminal, una vez ahi escriba 
    1- python manage.py makemigrations
    2- python manage.py migrate
Para correr el proyecto escriba python manage.py runserver.

Para la aplicación front en Vuejs, una vez descargado la aplicación abre una nueva terminal y escriba 
    1- npm install para agregar las dependencias del proyecto.
    2- npm run serve para correr la aplicación
una vez terminado se podrá visualizar la aplicación con las urls que le saldrá en la terminal
