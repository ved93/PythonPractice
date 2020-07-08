

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







##example
h= Holding('AA','2019-09-09',13,32.2)
h.name


import  csv

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        # headers = next(rows)
        for row in rows:
            h = Holding(row[0], row[1], row[2],row[3]) 
            portfolio.append(h)

    return portfolio

 
#this will return list of holding opbjects 
portfolio = read_portfolio("*.csv")
total = 0 
for h in portfolio:
    total+=h.shares*h.price

names = [h.names for h in portfolio]    


import a_table

table.print_table(portfolio, ['name', 'shares'])


formatter = table.TextTableFormatter()
table.print_table_new(portfolio, ['name', 'shares'], formatter)



formatter= table.create_formatter('text')()


