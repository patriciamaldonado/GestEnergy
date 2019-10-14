# Proyecto IV - GestEnergy
Documentación adicional del proyecto.

## Índice
* [Descripción del proyecto](#descripcion)
* [Implementación](#implementacion)
* [Descripción de la clase](#clase)
* [Herramientas de construcción y prueba](#tests)
* [Integración contínua](#CI)
  * [Travis CI](#travis)
  * [shippable](#shi)


  <a name="descripcion"></a>
## Descripción

   Microservicio para la gestión clientes de una empresa de energia, en el que se podrán realizar búsquedas sobre datos de clientes.

  El motivo por el que solo se pueden obtener datos y no modificarlos,borrarlos o añadirlos, es porque esta pensada para trabajadores que no tendrán estos privilegios. Simplemente se encargarán de llamar al cliente para ofrecer nuevas ofertas, comprobar sus datos, ofrecerles la mejor opcion a cada uno y que asi tengan un contrato hecho a medida y acorde a sus horarios y estilos de vida.

  Todos los datos de clientes estarán almacenados en un archivo que contendrá: nombre, apellidos, dirección, estado(baja/alta), energía contratada (electricidad,gas), potencia, Cups, provincia,DNI, teléfono, dirección.


  <a name="implementacion"></a>
## Implementación

  - Para desarrollarla voy a utilizar el lenguaje **[Python](https://wiki.archlinux.org/index.php/Python)** y el framework **[Flask](http://flask.palletsprojects.com/en/1.1.x/)**.

  - Como entorno virtual de python utilizaré **[Pipenv](https://pipenv-es.readthedocs.io/es/latest/)**.

  - Los datos se almacenarán en una base de datos NoSQL, **[MongoDB](https://www.mongodb.com/es)**

  - Para el registro de logs uso de logstash (ELK) con la biblioteca **[logging](https://docs.python.org/3/library/logging.html)**

  - Para testear nuestra clase se usará [nosetest](https://nose.readthedocs.io/en/latest/).

  - Travis CI para [integración contínua](https://github.com/patriciamaldonado/GestEnergy/blob/master/docs/documentacion.md)

  <a name="clase"></a>
## Descripción de la clase


Se va a testear la clase Clientes. Esta clase consta de métodos para la búsqueda de información sobre un cliente.


- **mostrarClientes**: devuelve un listado con todos los clientes actuales.
- **busquedaPorNombre**: busca clientes filtrando por nombre.
- **busquedaPorDNI**: busca un cliente en concreto filtrando por DNI.
- **busquedaPorProvincia**: busca clientes filtrando por provincia.
- **busquedaPorEstado**: busca un cliente filtrando por estado(baja/alta). Útil para obtener por ejemplo todos los clientes de baja e ir llamándolos para convencerlos de que vuelvan a la compañia. O bien obtener los que estén de alta para llamarlos y mejorarles su tarifa.
- **busquedaPorRobinson**: busca un cliente a través de su DNI para comprobar si se trata de un cliente Robinson, si se trata de un cliente Robinson te indica con un mensaje que a ese cliente no se le pueden ofrecer ofertas, en caso contrario muestra la información de ese cliente. Esto es útil cuando se quiere saber con rapidez si se puede llamar a un cliente.

- [Enlace a la clase Clientes](https://github.com/patriciamaldonado/GestEnergy/blob/master/src/clientes.py)


  <a name="tests"></a>
## Herramientas de construcción y prueba
Para testear la clase Clientes, se ha usado nosetest. [[1]](#nosetest)

Ejecución de test:
>  nosetest test.py

Se testean todos los métodos de la clase y además del método para comprobar si se ha inicializado bien.
- **testBusquedaPorNombre**: Se testea que no se haya introducido un número, busqueda vacía y que exista ese nombre.
- **testBusquedaPorDNI**: Se testea que no se haya introducido una busqueda vacía y que exista ese DNI.
- **testBusquedaPorProvincia**:  Se comprueba que no se haya introducido un número, busqueda vacía y que exista la provincia que se introduzca.
- **testBusquedaPorEstado**: se comprueba que el estado que se haya introducido sea uno de los dos posibles (alta o baja), que no se introduzca un número, ni una búsqueda vacía.
- **testRobinson**: testea cuando un cliente introducido sea robinson devuelva el mensaje "No puede ofrecer ofertas a este cliente"

- [Enlace al archivo de test](https://github.com/patriciamaldonado/GestEnergy/blob/master/src/tests.py)

<a name="CI"></a>
## Integración continua

Para integración continua se va a usar Travis CI,éste clona el repositorio a un entorno virtual para construir y probar tu código. Es fundamental detectar todos los fallos para posteriormente desplegar una versión correcta.

<a name="travis"></a>
### Configuración Travis CI para Python

1. Para empezar hay que ingresar con nuestra cuenta de Github en [Travis](https://travis-ci.com/) y permitir el acceso al repositorio del proyecto.
2. Añadir un archivo .travis.yml en la raíz de nuestro repositorio, en este archivo se incluye el lenguaje, las versiones de python a probar,instalar librerias, ejecución de test...

      - Podemos añadir comandos para que se ejecuten antes de la instalación (before_install).Instalar la útima versión de pip                  (pip install -U pip),comprobar versión en la que se está ejecutando con (python --version)                     
      - Con respecto a las versiones elegidas para probar nuestro código en python, no es recomendable usar inferiores a la 3.X   ya que la versión 2.7 no podrá utlizarse a partir de 2020. Por este motivo se probará en las versiones 3.X.
      Se ha probado la versión 3.7  y la versión 3.7-dev, ya que estsa versiones son recientes y no han llegado a su end-of-life.
      -  Las dependencias que necesitamos para nuestro proyecto se definen en en archivo requirements.txt, actualmente solo contiene la versión de flask que se podría usar. Se instalan mediante el comando pip3 install -r requirements.txt.
      - Para la ejecución de los test se ha utlizado un Makefille que mediante la orden make tests, se situa en la carpeta contenedora del test y lo testea mediante nosetest.

3. Una vez que tengamos configurado nuestro archivo .travis.yml correctamente, cada vez que hagamos git push se verificará si se pasan los test o fallan.


    - [Archivo de travis](https://github.com/patriciamaldonado/GestEnergy/blob/master/.travis.yml)
    - [Requirements](https://github.com/patriciamaldonado/GestEnergy/blob/master/requirements.txt)
    - [Makefile](https://github.com/patriciamaldonado/GestEnergy/blob/master/Makefile)

<a name="shi"></a>
### Configuración shippable para Python

  Para configurar shippable tenemos que ingresar en la página [shippable](https://app.shippable.com) y permitir acceso a nuestra cuenta de Github.
  Creamos un archivo llamado .shippable.yml en el que añadimos el lenguaje, versiones del lenguaje a probar y los comandos necesarios para la ejecución de test.

  [Archivo de shippable](https://github.com/patriciamaldonado/GestEnergy/blob/master/.shippable.yml)

 Podemos comprobar que los test se han ejecutado correctamente.
   ![shi](shi.jpg)
   ![build](builshi.png)


### Bibliografía


- <a name="testeo :nosetest">[nosetest](https://github.com/patriciamaldonado/GestEnergy/blob/master/Makefile)</a>
