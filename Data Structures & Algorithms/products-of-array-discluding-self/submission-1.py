'''
    Time Complexity: O(n)
    Space Complexity: O(1), Since this array is mandatory for the soltuion not extra.
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Create list to hold our answers
        res = [1] * len(nums)

        # Left to right walk (Prefix)
        left_product = 1
        for i in range(len(nums)):
            res[i] = left_product
            left_product *= nums[i]

        # Right to left walk (Suffix)
        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right_product
            right_product *= nums[i]

        return res

'''
    True Brute Force (Without Division):
        For every single index, loop through the entire array again and multiply 
        all other numbers together from scratch.
            Time Complexity: O(n^2) due to the nested loops.
            Space Complexity: O(1) auxiliary space (ignoring the mandatory output array).
'''