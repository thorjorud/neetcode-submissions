'''
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)

    Where m is the number of strings and n is the length of the longest string.
    The space accounts for the amount of keys needed for our hashmap and the
    values we are storing. Keys value can have up to m strings where each string
    could be up to length of n (where n is the longest string in the strs list).
'''


from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord("a")] += 1
            anagram_map[tuple(key)].append(s)
        return list(anagram_map.values())

'''
    Brute Force Approach: You take each string and sort it and use that as the key
    for the hash map. The trade off here is that we rely on a sorting algorithm which slows
    our solution down some.
        Time: O(m * n log n)
        Space: O(m * n)
'''