class Solution:
    '''
    Time Complexity: O(log n)
        - Since we are doing a binary search our search space
        gets cut in half each iteration.
    Space Complexity: O(1)
        - We only use a small variable.
    '''
    def findMin(self, nums: List[int]) -> int:
        # Set up our two pointers.
        left, right = 0, len(nums) - 1

        # Loop until the pointers converge (meet at the same index).
        while left < right:
            # Calculate the mid point. Doing it this way prevents integer overflow in other languages like C, C++ or Java.
            mid = left + (right - left) // 2

            # If number at mid is larger then number on the right pointer
            # then we know we are at a peak. Our min must be in the right half
            # of the search space.
            if nums[mid] > nums[right]:
                left = mid + 1
            # Otherwise we must be in the dropoff range or right on the min!
            else:
                right = mid
            
        # We could return nums[left] or nums[right] since they are the same number.
        return nums[left]

    '''
    Brute Force Approach: Perform a standard linear search across the array.
    Iterate through each element to find the minimum value (or find the exact index where the current number is smaller than the previous number).
        - Time Complexity: O(n) because we might have to check every single element in the worst case.
        - Space Complexity: O(1) since no extra memory is needed.
    '''