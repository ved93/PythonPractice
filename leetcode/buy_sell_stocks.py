


def maxProfit(self, prices ) :
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit



class Solution:
    def maxProfit(self, prices) :
        if not prices: return 0
        sell_prc = max(prices)
        max_prf = 0
        for p in prices:
            if p < sell_prc:
                sell_prc = p
            max_prf = max(p - sell_prc, max_prf)
            
        return max_prf