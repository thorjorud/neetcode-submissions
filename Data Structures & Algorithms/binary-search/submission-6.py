class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] == target:
                return left

            if nums[right] == target:
                return right

            if target < nums[right]:
                right -= 1
            else:
                left += 1

        return -1

