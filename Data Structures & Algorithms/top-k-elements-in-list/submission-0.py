'''
Time Complexity: O(n)
Space Complexity: O(n)

We trade some space for a quicker speed.
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Build frequency map for every num in nums.
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        
        # Use bucket sort where each indice corresponds to the freq. (e.g. say 2 appears twice, then 2 would go in buckets[2])
        buckets = [[]for _ in range(len(nums) + 1)]

        # Add each num to its correct bucket.
        for num, freq in num_count.items():
            buckets[freq].append(num)

        result = []
        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result