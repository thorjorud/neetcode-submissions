class Solution:
    '''
    Time: O(n)
    Space: O(n)
    '''
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

    