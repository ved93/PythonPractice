




class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
#         i, j = 0, len(nums)-1
#         while i <= j:
#             if nums[i]==target:
                
#                 return i
#             i= i+1
#         return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1
                
        