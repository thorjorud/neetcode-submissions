class Solution:
    def isValid(self, s: str) -> bool:
        close_key = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }
        stack = []

        for char in s:
            if char in close_key:
                if not stack or stack[-1] != close_key[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0