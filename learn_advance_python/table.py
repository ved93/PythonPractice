

def print_table(objects, colnames):
    #emitb table headers
    for colname in colnames:
        print('{:>10s}'.format(colname), end = ' ')
    print()

    for obj in objects:
        #emit of a row of table data
        for colname in colnames:
            #below returns the value of the colname
            print('{:>10s}'.format(str(getattr(obj,colname))), end= ' ')
        print()



#2nd version
def print_table_new(objects, colnames, formatter):
    formatter.headings(colnames)
    for obj in objects:
        #emit of a row of table data
        for colname in colnames:
            #below returns the value of the colname
            print('{:>10s}'.format(str(getattr(obj,colname))), end= ' ')
        print()


import sys

class TableFormatter(object):
    def __init__(self,outfile= None):
        if outfile ==None:
            outfile =sys.stdout
        self.outfile = outfile


    #serves a design spec for making tables (use inheriuctance to customise) 
    def headings(self,headers):
        raise NotImplementedError

    def row(self,rowdata):
        raise  NotImplementedError

class TextTableFormatter(TableFormatter):
    def headings(self,headers):
        for header in headers:
            print('{:>10s}'.format(header), end = ' ')
        print()

    def row(self,rowdata):
        for item in rowdata:
            print('{:>10s}'.format(item), end = ' ')
        print()

class CSVTableFormatter(TableFormatter):
    def headings(self,headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))
