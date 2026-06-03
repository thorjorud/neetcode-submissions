class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # We use a hash set for O(1) lookups to track numbers we've seen.
        for num in nums:
            if num in seen: 
                return True
            seen.add(num) 
        return False 
'''
Time Complexity: O(n)
Space Complexity: O(n)
We traded some space for a faster speed.
'''