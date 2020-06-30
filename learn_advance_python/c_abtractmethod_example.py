

import sys
from abc import ABC,abstractmethod

#using abstrcatmethod enforces implementation
#2nd way- use instance type in your func or method-- check print method


class TableFormatter(ABC):
    def __init__(self,outfile= None):
        if outfile ==None:
            outfile =sys.stdout
        self.outfile = outfile


    #serves a design spec for making tables (use inheriuctance to customise) 
    @abstractmethod
    def headings(self,headers):
        pass

    @abstractmethod
    def row(self,rowdata):
        pass



def print_table(objects, colnames, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError('formatter must be a table formatter')


    formatter.headings(colnames)
    for obj in objects:
        #emit of a row of table data
        for colname in colnames:
            #below returns the value of the colname
            print('{:>10s}'.format(str(getattr(obj,colname))), end= ' ')
        print()