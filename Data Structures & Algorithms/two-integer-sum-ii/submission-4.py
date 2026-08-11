class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            curr_sum = numbers[left] + numbers[right]

            if curr_sum == target:
                return [left + 1, right + 1]

            elif curr_sum < target:
                left += 1 # Move left pointer in by one to find bigger curr_sum.
            
            # If curr_sum > target.
            else:
                right -= 1 # Move right pointer in by one to find smaller curr_sum.