# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note:

# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:

# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false





class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        
        def word_break(s):
            if s == "": return True
            if s in dp: return dp[s]
            for word in wordDict:
                print(word)
                if word == s[:len(word)] and word_break(s[len(word):]):
                    dp[s] = True
                    return True
                dp[s] = False
                print(dp)
            return False
        
        return word_break(s)


#https://leetcode.com/problems/word-break/discuss/726060/Simple-Iterative-Python-Solution
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        # Instantiate a list of size N with boolean values representing each index of the string.
        canBreak = [True] + [False]*N
        for index in range(N):
            if not canBreak[index]:
                continue
                
            # iterate through everyword in wordDict
            for word in wordDict:
                if s[index:index+len(word)] == word:
                    canBreak[index+len(word)] = True # mark the breakpoints where the string can be broken. 
                    
        return canBreak[-1]        