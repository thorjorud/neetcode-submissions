class Solution:
    '''
    Time Complexity: O(n)
    Space Complexity: O(n)
        - n is the size of the ans array.
    '''
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)

        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        
        return ans