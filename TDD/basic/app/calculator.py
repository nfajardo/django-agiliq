class Calculator(object):

    def __init__(self):
        # tipos de datos numericos
        self.number_types = (int, float, complex)
 
    def add(self, x, y):
        # controlando excepcion de datos no numericos        
        if isinstance(x, self.number_types) and isinstance(y, self.number_types):
            return x + y
        else:
            raise TypeError
    
    # a veces no es obvio porque nuestras pruebas no pasan
    # vamos a escribir una funcion mal sin darnos cuenta (en realidad es aproposito)
    # y hacer debug con declaraciones Print

    def rest_bad(self, x, y):
        if isinstance(x, self.number_types) and isinstance(y, self.number_types):
            print('X is: {}'.format(x))
            print('Y is: {}'.format(y))
            result = x + y # seguro es la 1am, hiciste copy paste y se te olvido cambiar el signo
            print('Result is: {}'.format(result))
            return result
        else:
            raise TypeError

    # ahora nuestra funcion correcta 
    def rest_good(self, x, y):
        if isinstance(x, self.number_types) and isinstance(y, self.number_types):
            return x - y
        else:
            raise TypeError

