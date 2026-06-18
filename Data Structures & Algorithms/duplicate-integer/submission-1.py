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

'''
    Brute Force: We could compare each number in the list, but this would lead
    us to iterating over the same indexes multiple times. 
        Time: O(n^2)
        Space: O(1)
'''