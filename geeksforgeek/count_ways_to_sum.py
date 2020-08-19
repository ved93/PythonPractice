

# Given N, count the number of ways to express N as sum of 1, 3 and 4.

# Examples:

# Input :  N = 4
# Output : 4 
# Explanation: 1+1+1+1 
#              1+3
#              3+1 
#              4 

# Input : N = 5 
# Output : 6
# Explanation: 1 + 1 + 1 + 1 + 1
#              1 + 4
#              4 + 1
#              1 + 1 + 3
#              1 + 3 + 1
#              3 + 1 + 1


# Python program to illustrate the number of 
# ways to represent N as sum of 1, 3 and 4. 
  
# Function to count the number of 
# ways to represent n as sum of 1, 3 and 4 
def countWays(n): 
  
    DP = [0 for i in range(0, n + 1)] 
    print(DP)  
    # base cases 
    DP[0] = DP[1] = DP[2] = 1
    DP[3] = 2
  
    # Iterate for all values from 4 to n 
    for i in range(4, n + 1): 
        DP[i] = DP[i - 1] + DP[i - 3] + DP[i - 4] 
      
    return DP[n] 
  
      
# Driver code  

n = 4
print (countWays(n))