
# Have the function SimpleSymbols(str) take the str parameter being passed and determine if it is an acceptable sequence
#  by either returning the string true or false. The str parameter will be composed of + and = symbols with several
# letters between them (ie. ++d+===+c++==a) and for the string to be true each letter must be surrounded by a + symbol.
# So the string to the left would be false. The string will not be empty and will have at least one letter.

def SimpleSymbols(a_string):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for num in range(len(a_string)):
        if a_string[0] in letters or a_string[-1] in letters:
            return False
        elif a_string[num] in letters:
            if a_string[num-1] != '+' or a_string[num+1] != '+':
                return False
    return True




print(SimpleSymbols('++d+===+c++==a'))