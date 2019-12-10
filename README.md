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

 1. Clonar repositorio.

    > git clone  https://github.com/patriciamaldonado/GestEnergy.git

 2. Instalar Python3

    > $ sudo apt install python3

 3. Instalar dependencias
    > make install

4. Ejecutar tests unitarios y de integración

   > make tests

   > make testapi

   Se sitúa en la carpeta contenedora del archivo de tests y lo ejecuta mediante nosetest.

## Iniciar el servicio

Para el servicio se ha usado el gestor de procesos pm2 con gunicorn.
Previamente tenemos que haber instalado nodejs (sudo apt install nodejs), Python3 y
ejecutar make install.

Una vez instaladas las dependencias y clonado el repsositorio se podrá iniciar el servicio con el siguiente comando:
>  pm2 start 'gunicorn main:app -b 0000:5000 -w 2' --name "api"

Se iniciará en el navegador mediante la URL http://0.0.0.0:5000/


## Herramienta de construcción
> buildtool: Makefile

## Despliegue en un PaaS

> Despliegue: https://gest-energy.herokuapp.com/

## Despliegue Contenedor (Docker)

Contenedor: https://gestenergy-docker.herokuapp.com/

Contenedor: https://gestenergy.azurewebsites.net/

# Dockerhub

Dockerhub: https://hub.docker.com/r/pmaldonado/gestenergy

# provisionamiento

provision: provision/playbook.yml

## Documentación
Para documentación adicional vaya al siguiente enlace:
 - [Documentación adicional](https://github.com/patriciamaldonado/GestEnergy/blob/master/docs/documentacion.md)

Puede acceder a la sección deseada desde los siguientes enlaces:
- [Provisionamiento de máquinas virtuales](https://github.com/patriciamaldonado/GestEnergy/blob/master/docs/provisionamiento.md)

- [Despliegue Contenedor (Docker)](https://github.com/patriciamaldonado/GestEnergy/blob/master/docs/Docker.md)

- [Despliegue en un PaaS (heroku)](https://github.com/patriciamaldonado/GestEnergy/blob/master/docs/despliegue_paas.md)
- [Descripción y funcionamiento de la API](https://github.com/patriciamaldonado/GestEnergy/blob/master/docs/api.md)

- [Herramientas de construcción y prueba e Integración continua](https://github.com/patriciamaldonado/GestEnergy/blob/master/docs/CI_test.md)
- [Descrición de la clase](https://github.com/patriciamaldonado/GestEnergy/blob/master/docs/doc_clase.md)
