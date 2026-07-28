class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        Time Complexity: O(n)
            - [O(m) + O(1) + O(n - m)] = O(n)
        Space Complexity: O(1)
            - We only use basic variables which take up O(1) space.
        '''
        # If s1 > s2 then it is impossible for s2 to contain a permutation of s1.
        # There wouldn't be enough chars in s2.
        if len(s1) > len(s2):
            return False

        # Create freq arrays. Size 26 for letters 'a' through 'z'.
        s1_count, s2_count = [0] * 26, [0] * 26

        # Count freq for s1 and the VERY first window in s2.
        for i in range(len(s1)): # O(m) : m = len(s1)
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26): # O(1)
            if s1_count[i] == s2_count[i]:
                matches += 1


        left = 0
        for right in range(len(s1), len(s2)): # O(n - m) : n = len(s2), m = len(s1)
            if matches == 26:
                return True

            # Get the index of the char coming on the right.
            index = ord(s2[right]) - ord('a')
            s2_count[index] += 1

            # Update our match count.
            if s1_count[index] == s2_count[index]:
                matches += 1
            # If adding the letter on the right wrecked our match.
            elif s1_count[index] + 1 == s2_count[index]:
                matches -= 1

            # Get the index of the char leaving the window.
            index = ord(s2[left]) - ord('a')
            s2_count[index] -= 1

             # Update our match count.
            if s1_count[index] == s2_count[index]:
                matches += 1
            # If removing the letter on the left wrecked our match.
            elif s1_count[index] - 1 == s2_count[index]:
                matches -= 1
            
            # Move left pointer forward.
            left += 1
        
        # Check the very last window after the loop finishes
        return matches == 26

        '''
        Brute Force Approach: We first find the lengths of each str. m = len(s1), n = len(s2).
        We then sort s1 for upcoming comparisons. We can extract each substring of length m from s2.
        For each substring we sort it then compare it to the sorted version of s1.
        If they match then we can return true! Other wise we move on to the next substring.
            - Time Complexity: O(m log m) + [O(n - m + 1) * O(m) * O(m log m)]
                * O(m log m) + O(n - m) * O(m log m)
                    = O((n - m) * m log m)
            - Space Complexity: O(m)
                * Every time we slice the substring we create a new str of length m.
                * Every time we sort the substring that takes m time aswell.
        '''
            

        