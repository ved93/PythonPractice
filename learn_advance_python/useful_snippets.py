


#adding a path 
env PYTHONPATH = .. python


#to foramet print o/p
print('{:>10s}  {:>5d} {:>10.2f} '.format("e",18,34))
#string 10 char  5digit 10digitand2 decimal

#if want to store the output to file
out  = open('temp.txt','w')
print('{:>10s}  {:>5d} {:>10.2f} '.format("e",18,34) , file = out)
out.close()


#str join
','.join(string_names)


#use dict to pair the data i n zip
# dict with zip is highly useful

#take advantages dict comprehension . ie.e
prices  = {name:float(price) for name, price in zip(uniquee_names, price_data)}


