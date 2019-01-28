import unittest

from app.calculator import Calculator

class TddExample(unittest.TestCase):

    def test_add(self):
        cal = Calculator()
        result = cal.add(2,2)
        self.assertEqual(4, result)

"""
En este punto la funcion Calculator no ha sido definida, porq lo que nos da el siguiente error:

NameError: name 'Calculator' is not defined

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
"""

if __name__ == '__main__':
    unittest.main()