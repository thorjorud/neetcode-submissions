from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use a hash map to group anagrams into buckets.
        anagram_map = defaultdict(list)
        for s in strs:
            # The key is a unique identifer for each anagram.
            key = [0] * 26
            for c in s:
                # Subtracting the current ASCII value from ASCII value of 'a' gives us a perfect index for our key array. (0 - 25) which corresponds to A - Z.
                key[ord(c) - ord('a')] += 1
            anagram_map[tuple(key)].append(s)
        return list(anagram_map.values())
'''
Time Complexity: O(m * n)
Space Complexity: O(m * n)

m: Number of words in the strs array.
n: Length of each word in the strs array.
'''