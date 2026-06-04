class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths dont match, then they cannot be anagrams.
        if len(s) != len(t): 
            return False

        s_map = {}
        for c in s:
            s_map[c] = s_map.get(c, 0) + 1

        for c in t:
            # If t has a char that s doesn't or has more of a certain char then s does.
            if c not in s_map or s_map[c] == 0: 
                return False
            s_map[c] -= 1 

        return True
'''
Time Complexity: O(n + m)
Space Complexity: O(1) 

The space complexity is constant because we are limited
on the characters that can be in the strings.
'''
