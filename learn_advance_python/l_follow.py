
# watching a real time sta source with generator

import os
import time


def follow(filename):
    f = open(filename,'r')
    f.seek(0, os.SEEK_END)

    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue #retry
        yield line #emit a line

# f = open('.csv')
#lines = f.readlines()

for line in follow('stocklog.csv'):
    row = line.split(',')
    change= float(row[4])
    if change < 0:
        name = row[0]
        price  =row[1]
        print('{:>10s} {:>10s} {:>10.2f}'.format(name,price ,change))



##############
import csv

def parse_stock_data(lines):
    rows = csv.reader(lines)
    types = [str, float,str, str, float,float,float,int]
    converted = ([func(val) for func,val in zip(types,row)] for row in rows)

    return converted


lines = follow('.csv')
rows = parse_stock_data(lines)
negchange = (row for row in rows if row[4]< 0)
for row in negchange:
    name = row[0]
    price = row[1]
    change = row[4]
    print('{:>10s} {:>10.2f} {:>10.2f}'.format(name,price ,change))
