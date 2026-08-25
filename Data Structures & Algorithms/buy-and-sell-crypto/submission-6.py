class Solution:
    '''
    Time: O(n)
    Space: O(1)
    '''
    def maxProfit(self, prices: list[int]) -> int:
        left = 0 # Buy Day.
        max_profit = 0

        for right in range(1, len(prices)):
            profit = prices[right] - prices[left]
            if profit < 0:
                left = right # If found a cheaper day to buy.
                continue
            max_profit = max(max_profit, profit)
        
        return max_profit