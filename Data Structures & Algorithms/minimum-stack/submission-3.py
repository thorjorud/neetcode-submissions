class MinStack:
    '''
    Time: O(1)
    Space: O(n)
        - n is the max amount of elements added to either stack.
    '''
    def __init__(self):
        self.stack = []
        self.min_stack = [] # Keeps track of min value at each iteration.

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
            return
        
        min_val = self.min_stack[-1]
        self.min_stack.append(min(min_val, val)) # Push smaller value to min_stack.

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
