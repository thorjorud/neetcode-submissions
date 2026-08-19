class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        seen = set()

        nums.sort() 
        # Loops through outer numbers.
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                val = nums[i] + nums[right] + nums[left]
                if val == 0:
                    ans = (nums[i], nums[left], nums[right])
                    if ans in seen:
                        left += 1
                        right -= 1
                        continue
                    res.append([nums[i], nums[left], nums[right]])
                    seen.add(ans)

                    left += 1
                    right -= 1

                elif val < 0:
                    left += 1
                else:
                    right -= 1
        return res