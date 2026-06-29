class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        === INTERVIEW NOTES ===
        
        1. OPTIMIZED APPROACH (Stack)
           - Time Complexity: O(n)  | Space Complexity: O(n)
           - Explanation: Iterate through the tokens. Numbers are pushed onto a stack. 
             When an operator is hit, pop the top two numbers, apply the operation, 
             and push the result back.
           - Why it's better: A stack naturally processes the most recently seen 
             numbers first (Last-In, First-Out), matching the order of operations in RPN. 
             It allows us to evaluate the expression in a single pass without ever 
             backtracking or shifting array elements.
        
        2. BRUTE FORCE APPROACH (In-Place Array Mutation)
           - Time Complexity: O(n^2) | Space Complexity: O(1)
           - Explanation: Scan the array linearly to find an operator, compute the 
             result with its two left neighbors, delete those elements from the array, 
             insert the result, and restart the scan.
           - Why it's slow: Every time you delete/pop elements from the middle of an 
             array, all subsequent elements must shift over in memory, taking O(n) time. 
             Doing this for every operator degrades the total time to O(n^2).
        """
        stack = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                # Right Operand
                b = stack.pop()
                # Left Operand
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        
        return stack[0]

       
