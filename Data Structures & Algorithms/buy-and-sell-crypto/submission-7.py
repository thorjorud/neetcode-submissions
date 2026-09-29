class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        left = 0 # Buy day pointer.
        for right in range(1, len(prices)):
            curr_profit = prices[right] - prices[left]
            max_profit = max(max_profit, curr_profit)

            if prices[right] < prices[left]:
                left = right
        return max_profit