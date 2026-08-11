class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        l = 0
        
        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            
            # If we find a lower price than our current buy price, jump 'l' to 'r'
            if profit < 0:
                l = r
            else:
                max_profit = max(max_profit, profit)
                
        return max_profit
        