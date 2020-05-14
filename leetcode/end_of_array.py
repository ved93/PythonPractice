# Given an array of integers where each element represents the max number of steps that can be made forward from
# that element. The task is to find the minimum number of jumps to reach the end of the array (starting from the
# first element). If an element is 0, then cannot move through that element.

# https://leetcode.com/problems/jump-game-ii/

# Example:

# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
#     Jump 1 step from index 0 to 1, then 3 steps to the last index.


def min_jmp(arr):

    n = len(arr)
    right = prev_r = n - 1
    count = 0

    # We start from rightmost index and travesre array to find the leftmost index
    # from which we can reach index 'right'
    while True:
        for j in range(prev_r - 1, -1, -1):
            if j + arr[j] >= prev_r:
                right = j

        if prev_r != right:
            prev_r = right
        else:
            break

        count += 1

    return count if right == 0 else -1


# Enter the elements separated by a space
arr = list(map(int, input().split()))
print(min_jmp(arr))
