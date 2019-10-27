## Descripción de la api
Para crear la aplicación se ha utlizado el framework Flask.

A continuación se describen las diferentes rutas de la API.

| URI | Parámetros | Método | Descripción |
| :---: | :---: | :---: |---|
| / | | GET | Devuelve el estado de la api: status OK |
| /status | | GET | Devuelve el estado de la api: status OK |
| /mostrar | | GET | Devuelve un JSON con todos los clientes |
| /clientes | nombre | GET | Devuelve un JSON con ese cliente |
| /clientes | estado | GET | Devuelve un JSON con los clientes con ese estado (baja/alta)|
| /provincia | provincia| GET | Devuelve un JSON con los clientes de esa provincia |
| /robinson | DNI | GET | Devuelve un JSON con los datos del cliente perteneciente ese DNI (si no es Robinson) |
| /DNI | DNI| GET | Devuelve un JSON con los datos del cliente perteneciente ese DNI  |

 - Además de estas rutas, se ha controlado el error 404, cuando se introduce una URL incorrecta devuelve un JSON: {"error":"404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."}


- [Enlace al archivo de la api](https://github.com/patriciamaldonado/GestEnergy/blob/master/src/main.py)

## Ejecución de la api

Para ejecutar la api usamos el gestor de procesos pm2 con gunicorn.

> pm2 start 'gunicorn main:app -b 0000:5000 -w 2' --name "api"

En este ejemplo se ha iniciado la aplicación en la dirección y puerto 0000:5000 con 2 workers, además le establecemos un alias "api",
que nos servirá posteriormente para parar la api, reiniciarla,etc...
