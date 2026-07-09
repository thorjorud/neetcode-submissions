class Solution:
    '''
    Time Complexity: O(logn)
        - Each iteration elimimates half the search space (amount of numbers to search) by 2. 
    Space Complexity: O(1)
    '''
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            # Use this formula for mid to prevent int overflow in other languages.
            mid = l + ((r - l) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
    '''
    Brute Force Approach: We could do a linear search. This would require
    us to look each each element in the nums array. This is very inefficient if
    we have a really large array. This approach also ignores
    the fact that the array is already sorted. Plus we dont achieve O(logn) time.
        Time Complexity: O(n)
        Space Complexity: O(1)
    '''