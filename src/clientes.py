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
                n = False
                return n
            for cliente in self.clientes:
                if cliente["Nombre"] in nombre:
                        n.append(cliente)
            if not n:
                n = None
                return n
            return n

    def busquedaPorDNI(self,DNI):
            n = []
            for cliente in self.clientes:
                if cliente["DNI"] in DNI:
                        n.append(cliente)
            if not n:
                n = None
                return n
            return n
    def busquedaPorProvincia(self,provincia):
            n = []
            if type(provincia) == int:
                n = False
                return n
            for cliente in self.clientes:
                if cliente["Provincia"] in provincia:
                        n.append(cliente)
            if not n:
                n = None
                return n
            return n

    def busquedaPorEstado(self,estado):
            n = []
            if type(estado) == int:
                n = False
                return n
            for cliente in self.clientes:
                if cliente["Estado"] in estado:
                        n.append(cliente)
            if not n:
                n = None
                return n
            return n

    def busquedaPorRobinson(self,nombre):
            n = []
            if type(nombre) == int:
                n = False
                return n
            for i in self.clientes:
                if i["Nombre"] == nombre:
                        if i["Robinson"] == "no":
                            n.append(i)
                            return n
                        else:
                            n = None
                            return "No puede ofrecer ofertas a este cliente"

            return False
