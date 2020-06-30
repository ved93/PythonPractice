
from functools import wraps

def logged(func):
    #idea: give me a func i will put lohgging around it

    print('adding logging to ', func.__name__)

    @wraps(func)
    def wrapper(*args, **kwargs):
        print('calling ', func.__name__)
        return func(*args, **kwargs)
    
    return wrapper



################# Decorators with arguments. It can print any message you want to print for any function #######
def logformat(fmt):

    def logged(func):
        #idea: give me a func i will put lohgging around it

        print('adding logging to ', func.__name__)

        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func =func))
            return func(*args, **kwargs)
        
        return wrapper
    return logged


##calling
logged  = logformat('You are calling {func.__name__}')   #this is similar first decorator also

#now put this before any funct

@logged
def add(x,y):
    z=x+y 
    return  z


#creating class decorators-- This will just work like func decorator for all class emthod
def logmethods(cls):
    for key, value in list(vars(cls).items()):
        if callable(value):
            #is it a method? if so, decorate
            setattr(cls,key,logged(value))
    return cls    

