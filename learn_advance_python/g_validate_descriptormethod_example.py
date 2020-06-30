
#this is descriptor example
# this is useful when you want to validate lot of attributes and donyt want tp write propert methods for each attribute
#it badsically supervise th attribute

class Integer():
    def __init__(self,name):
        self.name = name

    def __get__(self,instance, cls):
        return instance.__dict__[self.name]

    def __set__(self,instance, value):
        if not isinstance(value, int):
            raise TypeError('expected int')
        instance.__dict__[self.name] = value

    
class Float():
    def __init__(self,name):
        self.name = name

    def __get__(self,instance, cls):
        return instance.__dict__[self.name]

    def __set__(self,instance, value):
        if not isinstance(value, float):
            raise TypeError('expected float')
        instance.__dict__[self.name] = value    

class Holding(object):
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price




######################################### What if we use inheritance to reduce the amt of code ##########################

class Typed(object):
    expected_type = object

    def __init__(self,name):
        self.name = name

    def __get__(self,instance, cls):
        return instance.__dict__[self.name]

    def __set__(self,instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('expected {} '.format(self.expected_type))
        instance.__dict__[self.name] = value       

class Integer(Typed):
    expected_type =int
class Integer(Typed):
    expected_type =float
class String(Typed):
    expected_type =str

class Holding(object):
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price


    
