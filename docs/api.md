## Descripción de la api


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

- [Enlace al archivo de la api](https://github.com/patriciamaldonado/GestEnergy/blob/master/src/main.py)
