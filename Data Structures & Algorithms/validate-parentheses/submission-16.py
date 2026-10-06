class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }

        stack = []

        for c in s:
            if c in close_to_open and stack:
                if stack[-1] == close_to_open[c]:
                    stack.pop()
                    continue
            stack.append(c)

        return len(stack) == 0