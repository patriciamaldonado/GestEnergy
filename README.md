
# GestEnergy (Gestión empresa Energia)

### Descripción

 Microservicio para la gestión clientes de una empresa de energia, en el que se podrán realizar búsquedas sobre datos de clientes.

Todos los datos de clientes estarán almacenados en un archivo que contendrá: nombre, apellidos, dirección, estado(baja/alta), energía contratada (electricidad,gas), potencia, Cups, ciudad, provincia,DNI, teléfono...

El fin de este proyecto es obtener búsquedas personalizadas a los trabajadores, para ofrecer nuevas ofertas a los clientes.

Como por ejemplo se quieren obtener datos sobre:

- clientes que estén actualmente de baja.
- clientes de una determinada ciudad.
- un cliente en concreto filtrando por DNI.


### Herramientas

- Para desarrollarla voy a utilizar el lenguaje **[Python](https://wiki.archlinux.org/index.php/Python)** y el framework **[Flask](http://flask.palletsprojects.com/en/1.1.x/)**.

- Como entorno virtual de python utilizaré **[virtualenv](https://wiki.archlinux.org/index.php/Python_(Espa%C3%B1ol)/Virtual_environment_(Espa%C3%B1ol))**.

- Los datos se almacenarán en una base de datos NoSQL, **[MongoDB](https://www.mongodb.com/es)**

- Como sistema de logs se va a usar **[logging](https://docs.python.org/3/library/logging.html)**, un módulo de Python.
