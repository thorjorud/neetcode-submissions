class Solution:
    '''
        Time Complexity: O(n)
        Space Complexity: O(1)
    '''
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]
            
            elif current_sum > target:
                right -= 1
            
            else:
                left += 1

    '''
         Brute Force Approach: You would use two nested for loops to manually check each
        pair until you found one that added up to the target. This is slow because if the 
        pair is at the end of the numbers array and say it has size 1,000 you would need
        to do up to 1,000,000 operations.
            Time Complexity: O(n^2)
            Space Complexity: O(1)
        
        Bonus Approach: You could use a hash map like we did in the original two sum from 
        arrays and hashing. BUT we would not get constant space.
            Time Complexity: O(n)
            Space Complexity: O(n)
    '''