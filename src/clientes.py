import unittest
import json



class Clientes:



    def __init__(self):
        with open('data/datosClientes.json', 'r') as f:
                self.clientes = json.load(f)

    def mostrarClientes(self):
        with open('datosClientes.json', 'r') as f:
            listado = self.clientes = json.load(f)
        return listado


    def busquedaPorNombre(self,nombre):
        n = []
        if type(nombre) == int:
            return False
        for i in self.clientes:
            if i["nombre"] == nombre:
                n.append(i)
                return n
        return False
