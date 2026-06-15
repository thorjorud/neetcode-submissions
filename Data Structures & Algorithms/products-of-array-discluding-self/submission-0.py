'''
    Time Complexity: O(n)
    Space Complexity: O(n)
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