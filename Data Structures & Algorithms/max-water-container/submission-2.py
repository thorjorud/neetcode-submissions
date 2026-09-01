class Solution:
    '''
    Time: O(n)
    Space: O(1)
    '''
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_water = 0

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            curr_water = width * height

            max_water = max(max_water, curr_water)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_water