
# Ebelow example shows why its important to implement special  methods as otherwise custom class wont work if 
# you n eed iterator. MNethods implemented are based on iusecases if you have diff usecase you =have to look up in reference
# If you want multiple other methods like append sort then use get atttr method


import  csv

class Holding(object):
    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    def cost(self):
        return self.price*self.shares


    def sell(self,nshares):
        self.shares-= nshares  




class Portfolio(object):
    def __init__(self):
        self.holdings = []


    def __getattr__(self, name):
        return getattr(self.holdings,name)



    @classmethod
    def from_csv(cls,filename):
        self = cls()
        with open(filename, 'r') as f:
            rows = csv.reader(f)
            # headers = next(rows)
            for row in rows:
                h = Holding(row[0], row[1], row[2],row[3]) 
                self.holdings.append(h)

    def total_cost(self):
        return sum([h.shares*h.price for h in self.holdings])

    def __len__(self):
        return len(self.holdings)

    def __getitem__(self,n):
        return self.holdings[n]
    def __iter__(self):
        return self.holdings.__iter__()







