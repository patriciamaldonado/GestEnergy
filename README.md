
# GestEnergy (Gestión empresa Energia)

### Descripción

 Microservicio para la gestión clientes de una empresa de energia, en el que se podrán realizar búsquedas sobre datos de clientes.

Todos los datos de clientes estarán almacenados en un archivo que contendrá: nombre, apellidos, dirección, estado(baja/alta), energía contratada (electricidad,gas), potencia, cup, ciudad, provincia...

El fin de este proyecto es obtener búsquedas personalizadas a los trabajadores, para ofrecer nuevas ofertas a los clientes.

Como por ejemplo se quieren obtener datos sobre:

- clientes que estén actualmente de baja.
- clientes de una determinada ciudad.
- un cliente en concreto filtrando por DNI.


### Herramientas

- Para desarrollarla voy a utilizar el lenguaje Python y el framework flask.

- Como entorno virtual de python utilizaré virtualenv.

- Los datos en principio se guardán en una base de datos NoSQL, MongoDB.
