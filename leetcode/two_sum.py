# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         i = 0
#         n = len(nums)
#         while i <= n:
#             for j in range(i,n):
#                 if nums[i]+nums[j] == target :
#                     return [i,j]
#             i = i+1

# def two_sum(nums, target):


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        r = []

        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in r:
                return [i, nums.index(temp)]

            r.append(nums[i])


#
# nums =   list(map(int,input().split()))
# target =  int(input())


if __name__ == "__main__":
    solution = Solution()
    # solution.twoSum(nums, target)
    print(solution.twoSum([2, 7, 11, 15], 9))
