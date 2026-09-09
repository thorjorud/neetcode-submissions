class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_1, len_2 = len(s1), len(s2)

        if len_1 > len_2:
            return False

        s1_freq, s2_freq = [0] * 26, [0] * 26

        for c in s1:
            s1_freq[ord(c) - ord('a')] += 1

        for i in range(len_1):
            s2_freq[ord(s2[i]) - ord('a')] += 1

        if s1_freq == s2_freq:
            return True

        for i in range(len_1, len_2):
            s2_freq[ord(s2[i]) - ord('a')] += 1
            s2_freq[ord(s2[i - len_1]) - ord('a')] -= 1

            if s1_freq == s2_freq:
                return True
        
        return False