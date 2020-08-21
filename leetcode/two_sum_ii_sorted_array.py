# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.


class Solution:
    def twoSum(self, numbers , target ):
    # def two_sum(self, nums, target):
        l,r = 0,len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r]== target:
                return (l+1,r+1)
            if numbers[l]+numbers[r] > target:
                r = r-1
            else:
                l = l+1


# dictionary           
def twoSum2(self, numbers, target):
    dic = {}
    for i, num in enumerate(numbers):
        if target-num in dic:
            return [dic[target-num]+1, i+1]
        dic[num] = i
        