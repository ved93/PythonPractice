
#generators are one time use. Sol is build a class for it.

def grep(pattern, filename):
    with open(filename) as f:
        for line in f:
            if pattern in line:
                yield line


for line in grep('IBM','Data/portfolio.csv'):
    print(line)


#2nde way
f = open('.csv')
ibm = (line for line in f if 'IBM' in line)    



def countdown(n):
    print('counting from ', n)
    while n > 0:
        yield n
        n-=1
    print('done')

for x in countdown(5):
    print(x)


c = countdown(5)
c #nothing happen as c is iterator obj
it = c.__iter__()
it
it.__next__() #now only it will start print



#2nd way - if we want to use repeatedly
class Countdown(object):
    def __init__(self,start):
        self.start = start
    
    def __iter__(self):
        n =self.start
        while n > 0:
            yield n
            n-=1

c =Countdown(5)

for x in c:
    print(x)

#now youn can use this iterator multiple times    
