[![Build Status](https://travis-ci.com/patriciamaldonado/GestEnergy.svg?branch=master)](https://travis-ci.com/patriciamaldonado/GestEnergy)
# GestEnergy (Gestión empresa Energia)

## Descripción

 Microservicio para la gestión clientes de una empresa de energia, en el que se podrán realizar búsquedas sobre datos de clientes.

Todos los datos de clientes estarán almacenados en un archivo que contendrá: nombre, apellidos, dirección, estado(baja/alta), energía contratada (electricidad,gas), potencia, Cups, ciudad, provincia,DNI, teléfono...

El fin de este proyecto es obtener búsquedas personalizadas a los trabajadores, para ofrecer nuevas ofertas a los clientes.

## Funcionalidades

Se podrán obtener datos de clientes realizando:

- Búsquedas por estado: baja/alta.
- Búsquedas por provincia.
- Búsqueda de un cliente en concreto filtrando por DNI.
- Búsqueda por nombre.
- Búsqueda para comprobar si se trata de un cliente Robinson.
- Mostrar listado completo de clientes.


## Ejecución de tests

 1. Clonar respositorio.

    > git clone  https://github.com/patriciamaldonado/GestEnergy.git

 2. Instalar Python3

    > $ sudo apt install python3

 3. Instalar nosetest
    > make install

    Al ejecutar make install ya se encarga de instalar pip3 y nose. ( pip3 install -U pip,  pip3 install nose)


4. Ejecutar tests
   > make tests

   Se sitúa en la carpeta contenedora del archivo de tests y lo ejecuta mediante nosetest.


## Documentación
Para documentación adicional vaya al siguiente enlace:
 - [Documentación adicional](https://github.com/patriciamaldonado/GestEnergy/blob/master/docs/documentacion.md)

Puede acceder a la sección deseada desde los siguientes enlaces:

- [Descrición de la clase](https://github.com/patriciamaldonado/GestEnergy/blob/master/docs/doc_clase.md)
- [Herramientas de construcción y prueba e Integración continua](https://github.com/patriciamaldonado/GestEnergy/blob/master/docs/CI_test.md)
