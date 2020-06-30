
def typed_property(name, expected_type):
    private_name = '_'+name

    @property
    def prop(self):
        return getattr(self, private_name)

    @prop.setter
    def prop(self, value):
        if not isinstance( value, expected_type):
            raise TypeError('Expected {}'.format(expected_type))

        setattr(self,private_name,value)

    return prop


Integer = lambda name:typed_property(name, int)
Float = lambda name:typed_property(name, float)
String = lambda name:typed_property(name, str)



class Holding(object):
    shares = Integer('shares')
    price = Float('price')
    name = String('name')


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


##example
h= Holding('AA','2019-09-09',13,32.2)
h  #this will use repr. Output only visible in interpreter mode.Remove str method to check output if you run script
print(h) #str method


