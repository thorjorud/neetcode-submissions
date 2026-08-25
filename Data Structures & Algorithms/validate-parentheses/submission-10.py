class Solution:
    '''
    Time: O(n)
    Space: O(n)
    '''
    def isValid(self, s: str) -> bool:
        close_to_open = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        stack = []

        for c in s:
            if c in close_to_open:
                if stack and stack.pop() == close_to_open[c]:
                    continue
                else:
                    return False
            stack.append(c)
        return len(stack) == 0
