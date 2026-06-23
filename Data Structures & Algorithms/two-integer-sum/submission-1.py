'''
Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_seen = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in nums_seen:
                return [nums_seen[diff], i]
            nums_seen[n] = i

'''
    Brute Force Approach: Use nested for loop to check each pair individually. Would use less space
    but would be a slower solution.
        Time Complexity: O(n^2)
        Space Complexity: O(1)
'''