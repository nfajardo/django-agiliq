import unittest

from app.calculator import Calculator

class TddExample(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        # test sum int
        result = self.calc.add(2, 11)
        self.assertEqual(13, result)
        # test sum float
        result1 = self.calc.add(12.55, 100.02)
        self.assertEqual(112.57, result1)

    def test_args_num(self):
        # return TypeError if x and y are not number
        self.assertRaises(TypeError, self.calc.add, 'one', 'three')
    
    def test_xarg_not_number(self):
        # return error message if x args is not number
        self.assertRaises(TypeError, self.calc.add, [1,2,3], 33.456)
 
    def test_yarg_not_number(self):
        # return error message if y args is not number
        self.assertRaises(TypeError, self.calc.add, 2, ('three'))


if __name__ == '__main__':
    unittest.main()