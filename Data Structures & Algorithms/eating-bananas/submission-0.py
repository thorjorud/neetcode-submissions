class Solution:
    '''
    Time Complexity: O(n log(m))
        - For every rate k we test we do binary searches which shrinks the 
        search space in half every step. Then for each binary search
        we need to loop through each pile where we have n number of piles.
    Space Complexity: O(1)
        - We only use a few variable for our pointers and keeping track of 
        the hours and rates k.
    '''
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Min eating speed by default is 1 and max is the size of the largest pile.
        left, right = 1, max(piles)
        # We know the max speed will work so we set that as the best k by default.
        best_k = right

        while left <= right:
            # Find mid point rate.
            k = (left + right) // 2
            '''
            total_hours is the amount of time it takes Koko to eat
            the piles with the current rate k.
            '''
            total_hours = 0
            # Test each pile with the current rate.
            for p in piles:
                total_hours += math.ceil(p / k)
            '''
            If total_hours is less then our hour limit then we found
            our current best rate. We then look into the left space in 
            search for an even slower rate.
            '''
            if total_hours <= h:
                best_k = k
                right = k - 1
            # Otherwise we look into the right space in search for a faster time.
            else:
                left = k + 1
            
        return best_k

        '''
        Brute Force Approach: We test each rate k starting at the absolute
        smallest rate of 1. We find the total hours for eating all the piles and then 
        check if that rate is <= h. If it is then great! That means we found the slowest
        rate, since we started checking at the min we know that the first one less
        then h is going to be the min rate.
            - Time Complexity: O(n * m)
                * n is the number of piles. m is the max number of bananas
                in a single pile (the worst-case speed we might have to test).
            - Space Complexity: O(1)
        '''
