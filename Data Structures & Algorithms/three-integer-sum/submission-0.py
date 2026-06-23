class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
            Time Complexity: O(n^2)
            Space Complexity: O(1) or O(n)
        '''
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            # If current num is equal to previous, then we skip.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Set up our pointers
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1

                    # If our left pointer has a duplicate then we skip it.
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1

        return res

'''
    Brute Force Approach: Use 3 nested loops and compare each number. Use a set
    to prevent duplicate triplets:
        Time Complexity: O(n^3)
        Space Complextiy: n
'''