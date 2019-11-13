
from flask import Flask,jsonify,request
import logging
import json
from .clientes import Clientes
import os

app = Flask(__name__)

import os


c = Clientes()

@app.route('/',methods=['GET'])
def principal():
#    app.logger.debug('Arranque de la aplicacion')
    status = {"status": "OK"}
    return json.dumps(status)

#Gestionamos el error 404, para cuando se introduzca una URL incorrecta
@app.errorhandler(404)
def page_not_found(e):
    #return 'URL incorrecta', 404
    return jsonify(error=str(e)), 404

@app.route('/status',methods=['GET'])
def status():
    status = {"status": "OK"}
    return json.dumps(status)

@app.route('/mostrar',methods=['GET'])
def mostrar():
    clientes = c.mostrarClientes()
    return jsonify(clientes)

@app.route('/clientes/<nombre>',methods=['GET'])
def busquedapornombre(nombre):

        clientes = c.busquedaPorNombre(nombre)
        return jsonify(clientes)


@app.route('/estado/<estado>',methods=['GET'])
def busquedaporestado(estado):

    clientes = c.busquedaPorEstado(estado)

    return jsonify(clientes)

@app.route('/provincia/<provincia>',methods=['GET'])
def busquedaporprovincia(provincia):

    clientes = c.busquedaPorProvincia(provincia)

    return jsonify(clientes)

@app.route('/robinson/<DNI>',methods=['GET'])
def busquedaporobinson(DNI):

    clientes = c.busquedaPorRobinson(DNI)

    return jsonify(clientes)

@app.route('/DNI/<DNI>',methods=['GET'])
def busquedaporDNI(DNI):

    clientes = c.busquedaPorDNI(DNI)

    return jsonify(clientes)


if __name__ == '__main__':
    #LOG_FILENAME = '/home/patri/Escritorio/errores.log'
    #logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
   # app.run(host='0.0.0.0')
   port = int(os.environ.get("PORT", 5000))

   app.run(host='0.0.0.0', port=port)
