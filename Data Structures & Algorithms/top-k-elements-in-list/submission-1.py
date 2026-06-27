'''
Time Complexity: O(n)
Space Complexity: O(n)
'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create frequency map
        num_map = {}
        for n in nums: 
            num_map[n] = num_map.get(n, 0) + 1

        # Create buckets to store nums, each bucket represents the freq so buckets[1] = nums occuring once.
        buckets = [[] for _ in range(len(nums) + 1)]

        # Fill the buckets up with nums.
        for num, freq in num_map.items():
            buckets[freq].append(num)

        res = []
        for i in range(len(nums), 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res

'''
    Brute Force Approach: First, create a frequency map of the numbers. 
    Then, convert the map into a list of elements/pairs and sort 
    them in descending order based on their frequencies. Finally, extract the first k elements from the sorted list.
        Time Complexity: O(n log n)
        Space Complexity: O(n)
'''