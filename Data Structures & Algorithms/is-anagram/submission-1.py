class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Time Complexity: O(n + m)
        Space Complexity: O(1) due to our lowercase English letter constraint.
        '''
        if len(s) != len(t):
            return False

        # Create freq map for s.
        s_map = {}
        for c in s:
            s_map[c] = s_map.get(c, 0) + 1

        # Compare each char in t with each char in s via the s_map (We are just cross checking the two strings)
        for c in t:
            if c not in s_map or s_map[c] == 0:
                return False
            s_map[c] -= 1

        return True

        '''
        Brute Force Approach: You sort both strings and then compare them.
            Time Complexity: O(n log n + m log m)
                - Sorting takes the length of the string + log.
            Space Complexity: O(1) or O(n + m)
                - Depending on the sorting algorithm used. An inplace sort
                  would be constant time.
        '''