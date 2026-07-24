class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Time Complexity: O(n)
        Space Complexity: O(m) or O(1)
            - m is the amount of unique chars in s.
            since our map can have a max of 26 key-value pairs we could 
            also say the space is O(1).

        Brute Force Approach: Find every possible substring and keep track
        of the largest substring that has a valid amount of replacements. You would
        need to use 2 nested for loops, an outer one to keep track of the start
        of the substring and the inner to keep track of the end.
            - Time Complexity: O(n^2)
            - Space Complexity: O(m) or O(1)
                - Same logic as optimal approach.
        '''
        count = {} # Freq map.
        maxf = 0 # Keep track of most freqent char.
        res = 0
        l = 0

        for r in range(len(s)):

            count[s[r]] = count.get(s[r], 0) + 1 # Update freq map.

            # Update max frequency.
            maxf = max(maxf, count[s[r]])

            # Replacements needed to keep the substring consecutive = (r - l + 1) - maxf.
            # While replacements is greater then k (most amount of replacements we can do).
            # Decrement by 1 and move l forward and until window is valid again.
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            # If window is valid calculate its size and update res.
            curr_window_size = (r - l + 1)
            res = max(res, curr_window_size)

        return res