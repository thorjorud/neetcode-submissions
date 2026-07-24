class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Time Complexity: O(n)
        Space Complexity: O(m) or O(1)
            - m is the amount of unique characters found in the input
            string s. We can have atmost 26 key value pairs.
        '''
        count = {} # Tracks character frequencies.
        res = 0
        l = 0
        maxf = 0 # Highest frequency of a single character in the window.

        for r in range(len(s)):
            # Adds character s[r] to the frequency map.
            count[s[r]] = count.get(s[r], 0) + 1

            # Update max frequency seen so far.
            maxf = max(maxf, count[s[r]])

            # Current Window length: (r - l + 1).
            # Current replacements needed to stay valid = current window length - max frequency character.
            # If replacements exceeds k (the most replacements we can perform) we move the left
            # pointer up until our replacements number is valid.
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1 # Remove character at left pointer from frequency.
                l += 1 # Move left pointer forward.

            res = max(res, r - l + 1)

        return res

    '''
    Brute Force Approach: We can manually check every possible substring in the input string
    using an outer loop to keep track of the start of the substring and an inner
    loop to keep track of the end of the substring. For every new substring
    we generate a new freq map and maxf integer. We check if the amount of replacements needed
    is <= k for every sequence and update res. At the end we return res. res is the size
    of the longest substring which contains only one char.
        - Time Complexity: O(n^2)
        - Space Complexity: O(m) or O(1)
            - m is the amount of unique characters in the input string s.

    '''