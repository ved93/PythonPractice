
# https://leetcode.com/problems/climbing-stairs/



class Solution:

    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        
        
        return self.climbStairs(n-1)+self.climbStairs(n-2)



#2nd way
# Bottom up, O(n) space
def climbStairs2(self, n):
    if n == 1:
        return 1
    res = [-1 for i in range(n+1)]
    res[0] = 1
    res[1] = 1
    
    for i in range(2,n+1):
        res[i] = res[i-1]+res[i-2]
        
    return res[-1]


# Bottom up, constant space
def climbStairs3(self, n):
    if n == 1:
        return 1
    a, b = 1, 2
    for i in range(2, n):
        tmp = b
        b = a+b
        a = tmp
    return b

# Top down + memorization (list)
def climbStairs4(self, n):
    if n == 1:
        return 1
    dic = [-1 for i in range(n)]
    dic[0], dic[1] = 1, 2
    return self.helper(n-1, dic)
    
def helper(self, n, dic):
    if dic[n] < 0:
        dic[n] = self.helper(n-1, dic)+self.helper(n-2, dic)
    return dic[n]
    
# Top down + memorization (dictionary)  
def __init__(self):
    self.dic = {1:1, 2:2}
    
def climbStairs(self, n):
    if n not in self.dic:
        self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
    return self.dic[n]







class Solution:
    def climbStairs(self, n: int):
        ## RC ##
        ## APPROACH 1 : RECURSION ##
        # must do approach to understand concept.
        # Recursion has :
        # 1. base condition (to exit loop) i.e i>n => return 0  or i==n return 1
        # 2. recursive call : climb(i+1,n) + climb(i+2,n)
        
        ## APPROACH 2 : DP ##
        #   1. top can be reached from (N-1)th Step or (N-2)th Step i.e ===> dp[N-1] + dp[N-2]
        #   2. base case :                                              No of ways
        #   0 steps     ===>    0 step                                      0
        #   1 steps     ===>    1 step                                      1   
        #   2 steps     ===>    (1 + 1 steps) or (2 steps)                  2       
        
        #   FINDING DP PATTERN
        #   3 steps     ===>    (1+1+1) (1+2) (2+1) (3)                     3
        #   4 steps     ===>    (1+1+1+1) (1+2+1) (2+1+1) (1+1+2) (2+2)     5   (pattern found n-1 + n-2 )
        
        if(n==1): return 1
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]                           # last position will have solution.