class Solution:
    def isValid(self, s: str) -> bool:
        '''
            Time Complexity: O(n)
            Space Complexity: O(n)
        '''
        close_to_open = {
            ")" : "(",
            "}" : "{",
            "]" : "["  
                        }

        stack = []

        for char in s:
            if char in close_to_open:
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0

        '''
            Brute Force Approach: You use a while loop and loop while either
            "()", "{}" or "[]" or in the string. If they are then you replace them with
            an empty string. At the very end your string should be empty if it is then 
            you return True otherwise return False.
                Time Complexity: O(n^2)
                    - Since we loop through each of up to n / 2 pairs, and when we replace
                      the chars with an empty string that takes n aswell since Python 
                      needs to loop through the string. Since they are nested we get O(n^2).
                Space Complexity: O(n)
                    - When we replace the chars with the empty string using
                      replace() Python allocates a new copy of the string with the
                      characters removed. This scales with the input size of O(n).
        '''