class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        max_profit = 0
        min_price = float('inf')

        for p in prices:
            if p < min_price:
                min_price = p
            else:
                max_profit = max(max_profit, p - min_price)
        
        return max_profit

        '''
        Brute Force Approach: We could use a nested for loop and compare
        every possible buy and sell combo. 
            Time Complexity: O(n^2)
                - Would result in a Time Limit Exceeded (TLE) on larger inputs.
            Space Complexity: O(1)
        '''
