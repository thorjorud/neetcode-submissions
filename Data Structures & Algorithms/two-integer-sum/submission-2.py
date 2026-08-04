class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {} # {num : index}

        for i, n in enumerate(nums):
            
            diff = target - n

            if diff in num_map:
                return([num_map[diff], i])
            else:
                    num_map[n] = i