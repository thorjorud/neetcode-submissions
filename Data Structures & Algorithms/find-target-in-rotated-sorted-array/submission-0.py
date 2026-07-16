class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Time Complexity: O(log n)
        Space Complexity: O(1)
        '''
        left, right = 0, len(nums) - 1

        while left <= right:
            # Calculate mid this way to prevent integer overflow in other languages.
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # If the number on the left pointer is smaller than or equal to the mid number
            # then we know the left side is the sorted side.
            if nums[left] <= nums[mid]:
                # Check if the target is OUTSIDE the bounds of this sorted left side.
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                # Otherwise target is on this side.
                else:
                    right = mid - 1
            # Otherwise we know the sorted side is the right side. 
            else:
                # Check if target is OUTSIDE the bounds of this sorted right side.
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                # Otherwise target is on this side.
                else:
                    left = mid + 1

        # Return -1 if we never find target.
        return -1

    '''
    Brute Force Approach: You can do a linear search. This would ignore the 
    fact that part of the input array is sorted and lead us to a linear time.
        - Time Complexity: O(n)
        - Space Complexity: O(1)
    '''