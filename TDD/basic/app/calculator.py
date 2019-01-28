class Calculator(object):

 
    def add(self, x, y):
        # tipos de datos numericos
        number_types = (int, float, complex)

        # controlando excepcion de datos no numericos        
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise TypeError
