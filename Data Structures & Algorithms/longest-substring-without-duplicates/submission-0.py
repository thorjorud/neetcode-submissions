class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Time Complexity: O(n)
            - Even though we have two loops both pointers 
            only iterate over each char up to one time.
        Space Complexity: O(m)
            - Our Hash Set hold up to the amount of unique chars in 
            the input str. Since Hash Sets cannot hold duplicates.
        '''
        char_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            # If we encounter a duplicate letter. We remove letters from 
            # the left until we remove the first copy of that letter.
            # Thus making the str unique again.
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # If we hit a unique letter we add it to the set.
            char_set.add(s[right])

            # After each unique letter we add, we re-check
            # to see if the current sequence we're on beats out
            # the current max_len.
            # Using the formula: right - left + 1 helps us determine the length.
            max_len = max(max_len, right - left + 1)
        
        return max_len

        '''
        Brute Force Approach:
        We use two nested loops to test every possible starting position. The outer loop 
        (left pointer) sets the start of the substring and initializes a fresh hash set. 
        The inner loop (right pointer) expands the substring character by character:
            - If the character is unique, add it to the set and update max_len.
            - If a duplicate is encountered, break out of the inner loop and advance the left pointer.

        Complexity:
            - Time: O(n^2) - Checking all valid substrings up until the first duplicate.
            - Space: O(m) - Where m is the number of unique printable ASCII characters stored in the set.
        '''