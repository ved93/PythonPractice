
def AlphabetSoup(a_string):
    list_of_chars = []

    for char in a_string.lower():
        list_of_chars.append(char)

    ordered_list = sorted(list_of_chars)
    alphabetical_string = ''.join(ordered_list)

    return alphabetical_string



print(AlphabetSoup('erryyujdwd'))