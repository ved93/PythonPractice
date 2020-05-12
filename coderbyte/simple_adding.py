# Have the function SimpleAdding(num) add up all the numbers from 1 to num. For the test cases,
# the parameter num will be any number from 1 to 1000.

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def SimpleAdding(num):

    if num > 0:
        num = num + SimpleAdding(num - 1)

    return num


print(SimpleAdding(int(input())))
