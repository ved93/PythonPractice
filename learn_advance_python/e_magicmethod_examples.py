


#tip 1
#repr method: It return nice formatted class object, makes debugging lot easier

#tip 2
#str method- nice formatted outpur string. almost same as repr. Check in  interpreter mode to understand

#tip 3
# property method- This is used when youn want to put validation or checks for a class obj check the example price
# 2nd use: when you wan to use computed method as attribute. i.e. now you can use cost as h.cost same as h.name etc
#check validate descriptor.py for next version of this

#tip 4
# code is verbose with property lets generalise this and reuses over and over again. this is basically typechecking .so reuseable
# 06_typedproperty- this will replace property andf take it out.


#extras
#h.name is same as h.__dict__['name']

class Holding(object):
    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, newprice):
        if not isinstance(newprice, float):
            raise TypeError('expected float')
        if newprice < 0 :
            raise ValueError('expected > 0')
        self._price = newprice
    


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


