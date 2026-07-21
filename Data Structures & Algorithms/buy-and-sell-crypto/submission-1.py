class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        left, right = 0, 1 # left = buy, right = sell
        max_profit = 0

        while right < len(prices):
            # If our sell day is worth more then our buy day.
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            # Otherwise if our sell day is worth less then we found a cheaper day to buy on.
            else:
                left = right

            # We always move the right pointer up to keep the window sliding.
            right += 1
        
        return max_profit

        '''
        Brute Force Approach: We could use a nested for loop and compare
        every possible buy and sell combo. 
            Time Complexity: O(n^2)
                - Would result in a Time Limit Exceeded (TLE) on larger inputs.
            Space Complexity: O(1)
        '''
