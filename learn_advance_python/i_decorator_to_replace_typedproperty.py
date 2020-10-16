


#http://zetcode.com/python/python-decorators/



#decorator example
from h_logcall import logformat,logmethods
logged  = logformat('You are calling {func.__name__}')  



@logmethods
class  Spam():
    # @logged
    def __init__(self, value):
        self.value =value






#replacing typedproperty


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
class Float(Typed):
    expected_type =float
class String(Typed):
    expected_type =str

def typed(cls):
    for key, value in vars(cls).items():
        if isinstance(value , Typed):
            value.name = key
    return cls

def validate(**kwargs):
    def decorate(cls):
        for name,val in kwargs.items():
            setattr(cls,name,val(name))
        return cls
    return decorate




@validate(name =String,shares =Integer,price =Float) #this will validate and its nice in look
# @typed
class Holding(object):
    # shares = Integer()
    # price = Float()
    # name = String()


    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    def __repr__(self):
        return 'Holding({!r}, {!r},{!r},{!r})'.format(self.name, self.date,self.shares, self.price)

    def __str__(self):
        return '{} shares of {} at ${:0.2f}'.format(self.shares, self.name, self.price)

    @property
    def cost(self):
        return self.price*self.shares


    def sell(self,nshares):
        self.shares-= nshares  


