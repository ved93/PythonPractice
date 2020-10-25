
#https://leetcode.com/problems/valid-palindrome/solution/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # filtered_chars = filter(lambda ch: ch.isalnum(), s)
        # lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)

        # filtered_chars_list = list(lowercase_filtered_chars)
        # reversed_chars_list = filtered_chars_list[::-1]

        # return filtered_chars_list == reversed_chars_list
        i, j = 0 , len(s)-1
        while i < j :
            while i < j and not s[i].isalnum() :
                i = i+1
            while i < j and not s[j].isalnum():
                j = j-1
                
            if i < j and s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
            
        return True
    
 
        

