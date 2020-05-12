#  Using the Python language, have the function ArrayAdditionI(arr) take the array of numbers stored in arr and return
# the string true if any combination of numbers in the array can be added up to equal the largest number in the array,
# otherwise return the string false. For example: if arr contains [4, 6, 23, 10, 1, 3] the output should return true
# because 4 + 6 + 10 + 3 = 23. The array will not be empty, will not contain all the same elements, and may contain
# negative numbers.


def ArrayAdditionI(arr):
    max_num = max(arr)
    possible_total = []
    arr.remove(max_num)

    arr = sorted(arr)

    for num in arr:
        possible_total.append(num)

        arr.remove(num)

        num_total = num
        for other_num in arr:

            possible_total.append(num + other_num)
            num_total = num_total + other_num
            possible_total.append(num_total)

    if max_num in possible_total:
        return True
    return False


print(ArrayAdditionI([4, 6, 23, 10, 1, 3]))
