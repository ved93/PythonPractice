
# Using the Python language, have the function TimeConvert(num) take the num parameter being passed and return the
# number of hours and minutes the parameter converts to (ie. if num = 63 then the output should be 1:3).
# Separate the number of hours and minutes with a colon.

def TimeConvert(int):
    return str(int//60) + ':' + str(int%60)

print(TimeConvert(136))