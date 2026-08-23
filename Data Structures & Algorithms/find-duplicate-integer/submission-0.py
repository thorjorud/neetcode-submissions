class Solution:
    '''
    Time Complexity: O(n)
    Space Complexity: 
    '''
    def findDuplicate(self, nums: List[int]) -> int:
        # Step One: Find the cycle.
        # Treat the array indeces as the next node to point to.
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow] # Moves one step at a time.
            fast = nums[nums[fast]] # Moves two steps at a time.

            if slow == fast: # If we found a cycle.
                break

        slow2 = nums[0] # Create new slow to identify duplicate.
        while slow != slow2:
            # Both move one step at a time.
            slow2 = nums[slow2]
            slow = nums[slow]
        
        return slow
