import unittest
from gestenergy import Clientes

class testClientes(unittest.TestCase):


    c = Clientes()

    def testInicializacion(self):
            c = Clientes()
            self.assertIsInstance(c,Clientes);


    def testBusquedaPorNombre(self):
            self.assertEqual(self.c.busquedaPorNombre(1), False,"Estas buscando un nombre, no puedes introducir un numero") # si introducimos un numero, la respuesta esperada seria false
            self.assertEqual(self.c.busquedaPorNombre(" "), None,"Busqueda vacia")
            self.assertIsNone(self.c.busquedaPorNombre("maria"),"No existe ese cliente")
        #    self.assertIsNone(self.c.busquedaPorNombre("Juan"),"No existe ese cliente") #Fallaria al existir


    def testBusquedaPorDNI(self):
            self.assertEqual(self.c.busquedaPorDNI(" "), None,"Busqueda vacia")
            self.assertIsNone(self.c.busquedaPorDNI("66666666A"),"No hay ningun cliente con ese DNI")
            #self.assertIsNone(self.c.busquedaPorDNI("66666666B"),"No hay ningun cliente con ese DNI")

    def testBusquedaPorProvincia(self):
            self.assertEqual(self.c.busquedaPorProvincia(1), False,"Estas buscando una provincia, no puedes introducir un numero")
            self.assertEqual(self.c.busquedaPorProvincia(" "), None,"Busqueda vacia")
            self.assertIsNone(self.c.busquedaPorProvincia("Malaga"),"No se encuentra esa provincia")

    def testBusquedaPorEstado(self):
            self.assertEqual(self.c.busquedaPorEstado(1), False,"Estas buscando un estado(baja/alta), no puedes introducir un numero")
            self.assertEqual(self.c.busquedaPorEstado(" "), None,"Busqueda vacia")
            self.assertIsNone(self.c.busquedaPorEstado("anulado"),"Solo pueden estar de alta o baja")


    def testRobinson(self):
            self.assertEqual(self.c.busquedaPorRobinson("77777777A"),"No puede ofrecer ofertas a este cliente")
            #self.assertEqual(self.c.busquedaPorRobinson("66666666B"),"No puede ofrecer ofertas a este cliente")


if __name__ == '__main__':
    unittest.main()
