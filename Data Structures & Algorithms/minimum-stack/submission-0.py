class MinStack:
    '''
    Time Complexity: O(1) for all operations
    Space Complexity: O(n)
    
    Why this approach instead of Brute Force?
    - Brute Force: We could use a single standard stack. However, every time 
      getMin() is called, we would have to iterate through the entire stack 
      to find the smallest number. This would take O(n) time.
    - Optimized (Below): By using an extra stack (min_stack) to record the 
      "prefix minimum" at every single stage, we can instantly retrieve the 
      minimum element in O(1) time, trading a bit of space for maximum speed.
    '''
    def __init__(self):
        self.stack =[]
        self.min_stack = []


    def push(self, val: int) -> None:
        # Main stack keeps track of overall history.
        self.stack.append(val)

        # If min_stack is not empty.
        if self.min_stack:
            # We want the min value for each stage.
            val = min(val, self.min_stack[-1])
        # Push whatever the current min is at this stage.
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:  
        return self.stack[-1]
        
    def getMin(self) -> int:
        # Return last value from min_stack since that one keeps track of mins.
        return self.min_stack[-1]