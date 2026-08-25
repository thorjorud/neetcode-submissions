from collections import Counter

class Solution:
    '''
    Time: O(n + m)
        - Build both freq maps where n = len(s) and m = len(t).
    Space: O(1)
        - Freq map can hold at most 26 key - value pairs.
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        

        