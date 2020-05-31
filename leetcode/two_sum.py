# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         i = 0
#         n = len(nums)
#         while i < n:
#             for j in range(i+1,n):
#                 if nums[i]+nums[j] == target :
#                     return [i,j]
#             i = i+1


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         r = []

#         for i in range(len(nums)):
#             temp = target - nums[i]
#             if temp in r:
#                 return [i, nums.index(temp)]

#             r.append(nums[i])


# #
# # nums =   list(map(int,input().split()))
# # target =  int(input())


# if __name__ == "__main__":
#     solution =   Solution()
#     # solution.twoSum(nums, target)
#     print(solution.twoSum([2, 7, 11, 15], 9))


from collections import defaultdict

# Returns the indices of two numbers that add up to the target
def two_sums(nums, target):

    lookup = defaultdict(list)
    for i, num in enumerate(nums):
        needed = target - num
        print(i, "  ", num, "  ", lookup)
        if needed in lookup:
            print(lookup[needed])
            return [lookup[needed][0], i]
        lookup[num].append(i)

    return None


print(two_sums([2, 7, 11, 15], 26))
print(two_sums([3, 3], 6))
