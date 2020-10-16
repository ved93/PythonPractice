


# A = [34,23,1,24,75,33,54,8]
# K = 60
# for num in A:
#     if num > 60:
#         print('dd')
#         continue 
#     print(num)


# def longestPalindrome(self, s):
#     res = ""
#     for i in range(len(s)):
#         # odd case, like "aba"
#         tmp = self.helper(s, i, i)
#         if len(tmp) > len(res):
#             res = tmp
#         # even case, like "abba"
#         tmp = self.helper(s, i, i+1)
#         if len(tmp) > len(res):
#             res = tmp
#     return res
 
# # get the longest palindrome, l, r are the middle indexes   
# # from inner to outer
# def helper(self, s, l, r):
#     while l >= 0 and r < len(s) and s[l] == s[r]:
#         l -= 1; r += 1
#     return s[l+1:r]

# # print(longestPalindrome("babad"))
# # print(longestPalindrome("cbbd"))



def climbStairs( n: int): 
    if n < 2:
        return 1
    
    
    count = climbStairs(n-1)+climbStairs(n-2)
    return count


print(climbStairs(5))