class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        l = 0 # Buy Day

        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r 
            else:
                max_profit = max(max_profit, profit)
        
        return max_profit