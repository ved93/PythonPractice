
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.


class Solution:
    def longestPalindrome(self, s: str) :
        m = ''  # Memory to remember a palindrome
        for i in range(len(s)):  # i = start, O = n
            for j in range(len(s), i, -1):  # j = end, O = n^2
                if len(m) >= j-i:  # To reduce time
                    break
                elif s[i:j] == s[i:j][::-1]:
                    m = s[i:j]
                    break
        return m




class Solution2:

    # starting at l,r expand outwards to find the biggest palindrome
    def palindromeAt(self,  s, l, r):    
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
    
    
    def longestPalindrome(self, s: str) :
        res = ""
        for i in range(len(s)):        
            odd  = self.palindromeAt(s, i, i)
            even = self.palindromeAt(s, i, i+1)

            res = max(res, odd, even, key=len)
        return res
