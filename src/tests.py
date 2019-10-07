import unittest
import sys
import os.path
src = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
+ '/src/')
sys.path.append(src)

from clientes import Clientes

class testClientes(unittest.TestCase):

    c = Clientes()
    def testBusquedaPorCliente(self):
        self.assertTrue("1", "Devuelve lo que tiene que devolver")
        self.assertEqual(self.c.busquedaPorNombre(1), False,"Estas buscando un nombre, no puedes introducir un numero") # si introducimos un numero, la respuesta esperada seria false
        self.assertEqual(self.c.busquedaPorNombre(" "), False,"Busqueda vacia")
        self.assertEqual(self.c.busquedaPorNombre("maria"), False,"No existe ese cliente")

if __name__ == '__main__':
    unittest.main()
