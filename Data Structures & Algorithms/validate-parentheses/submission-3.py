class Solution:
    def isValid(self, s: str) -> bool:
        close_key = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }
        stack = []

        for i in range(len(s)):
            if s[i] in close_key and stack:
                compare_val = stack.pop()
                if close_key[s[i]] == compare_val:
                    continue
            stack.append(s[i])

        return len(stack) == 0