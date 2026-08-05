from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        k = len(s1)
        s1_counter = Counter(s1)

        # Create freq map for first window.
        s2_counter = Counter(s2[:k])

        if s2_counter == s1_counter:
            return True

        for r in range(k, len(s2)):
            s2_counter[s2[r]] = s2_counter.get(s2[r], 0) + 1
            s2_counter[s2[r - k]] -= 1

            if s2_counter[s2[r - k]] == 0:
                del s2_counter[s2[r- k]]

            if s2_counter == s1_counter:
                return True

        return False
