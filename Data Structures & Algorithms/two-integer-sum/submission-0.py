class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Use a hash map for O(1) key lookup: (num : index)
        num_map = {}
        for i, num in enumerate(nums):
            # Number to search for in map.
            diff = target - num 
            if diff in num_map:
                return [num_map[diff], i]
            num_map[num] = i
'''
Time Complexity: O(n)
Space Complexity: O(n)
'''