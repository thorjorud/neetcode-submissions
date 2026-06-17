class Solution:
    '''
        Time Complexity: O(n)
        Space Complexity: O(n)
    '''
    def longestConsecutive(self, nums: List[int]) -> int:

        # Dump all numbers into a set for O(1) lookups.
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:

            # If num is the start of a streak. (Meaning a number smaller by one doesnt exist in the set)
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1

                # While streak is still valid.
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1

                # Update longest streak.
                longest_streak = max(longest_streak, current_streak)

        return longest_streak


''' 
    Brute Force Approach: We can loop through the array, and for each number, 
    scan the entire array to see if number + 1 exists.
    If it does, we scan the array again for number + 2, number + 3, etc. 
    This takes O(n^3) time. 
    
    Another approach would be to sort the array first (O(n log n)) 
    then walk it down from left to right and keep track of numbers that are right next to each other. 
'''