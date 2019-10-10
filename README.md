[![Build Status](https://travis-ci.com/patriciamaldonado/GestEnergy.svg?branch=master)](https://travis-ci.com/patriciamaldonado/GestEnergy)
# GestEnergy (Gestión empresa Energia)

## Descripción

 Microservicio para la gestión clientes de una empresa de energia, en el que se podrán realizar búsquedas sobre datos de clientes.

Todos los datos de clientes estarán almacenados en un archivo que contendrá: nombre, apellidos, dirección, estado(baja/alta), energía contratada (electricidad,gas), potencia, Cups, ciudad, provincia,DNI, teléfono...

El fin de este proyecto es obtener búsquedas personalizadas a los trabajadores, para ofrecer nuevas ofertas a los clientes.

## Funcionalidades

Se obtendrán datos sobre búsqueda de clientes:

- Por estado: baja/alta.
- Por provincia.
- Un cliente en concreto filtrando por DNI.
- ...


## Herramientas

- Para desarrollarla voy a utilizar el lenguaje **[Python](https://wiki.archlinux.org/index.php/Python)** y el framework **[Flask](http://flask.palletsprojects.com/en/1.1.x/)**.

- Como entorno virtual de python utilizaré **[Pipenv](https://pipenv-es.readthedocs.io/es/latest/)**.

- Los datos se almacenarán en una base de datos NoSQL, **[MongoDB](https://www.mongodb.com/es)**

- Para el registro de logs uso de logstash (ELK) con la biblioteca **[logging](https://docs.python.org/3/library/logging.html)**

- Para testear nuestra clase se usará [nosetest](https://nose.readthedocs.io/en/latest/).

- Travis CI para [integración contínua](https://github.com/patriciamaldonado/GestEnergy/blob/master/docs/documentacion.md)

## Ejecución test
 1. Clonar respositorio.
 2. Instalar Python3
 3. Instalar nosetest
 4. Ejecutar make tests
