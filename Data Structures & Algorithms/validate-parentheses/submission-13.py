class Solution:
    def isValid(self, s: str) -> bool:
        key = {
            ')' : '(',
            '}' : '{',
            ']' : '['
            }

        stack = []
        for c in s:
            if c in key:
                if stack and stack[-1] == key[c]:
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(c)
        return len(stack) == 0