import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('Datatres'.upper(), 'DATATRES')

    def test_isupper(self):
        self.assertTrue('DATA'.isupper())
        self.assertFalse('Data'.isupper())

    def test_split(self):
        s = 'Data Tres 60'
        self.assertEqual(s.split(), ['Data', 'Tres', '60'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_count(self):
        s = "la vamo a romper"
        c = len(s.split())
        self.assertEqual(len(s.split()), 4)
        self.assertTrue(len(s.split()) < 5)
        self.assertFalse(len(s.split()) > 15)
        self.assertIsInstance(s.split(), list)

# no es la mejor práctica tener las funciones y las pruebas en el mismo archivo
# pero esto es un ejercicio

def factorial(n): 
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

class TestFixture(unittest.TestCase):
    def setUp(self):
        print("Preparando el contexto de la prueba")
        self.num = 8
        self.num_test = [0, 1, 3, 5]
    
    def test_factorial(self):
        # esta es la prueba basica, pero que pasaria si
        # alguien intenta sacar el factorial de un string
        result = [factorial(n) for n in self.num_test]

        self.assertEqual(result, [1, 1, 6, 120])
        self.assertListEqual(result, [1, 1, 6, 120])
    
    def test_fact_type(self):
        # compruebo que efectivamente genera un error de tipo
        self.assertRaises(TypeError, factorial, 'three')
        self.assertRaises(TypeError, factorial, [1, 2, 3])

    def tearDown(self):
        print("limpiando el contexto")
        del(self.num_test)


if __name__ == '__main__':
    unittest.main()