# https://leetcode.com/problems/min-cost-climbing-stairs/discuss/394083/Four-Solutions-in-Python-3-(DP)-(Bottom-Up-and-Top-Down)


class Solution:
    def minCostClimbingStairs(self, cost ) :
        # Loop through every cost after the first two steps
        for i in range(2, len(cost)):
            # Update the cheapest cost to step here
            cost[i] += min(cost[i-2], cost[i-1])
        
        # Cheapest cost of the last two steps is the answer
        return min(cost[len(cost)-2], cost[len(cost)-1])




