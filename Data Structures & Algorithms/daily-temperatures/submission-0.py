class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        res = [0] * len(temperatures)
        stack = [] # [temp, index] pairs

        for i, t in enumerate(temperatures):
            # Check if current temp is warmer than temp at the top of the stack.
            while stack and t > stack[-1][0]:
                stack_t, stack_i = stack.pop()
                res[stack_i] = i - stack_i
            # Add current temp to the waiting room. (The Stack)
            stack.append([t, i])

        return res

    '''
    Brute Force Approach: Use a nested for loop to check for a warmer day.
    You would have to recheck numbers multiple times.
        Time Complexity: O(n^2)
        Space Complexity: O(1)
    '''