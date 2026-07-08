class Solution:
    '''
PROBLEM: Car Fleet
-------------------------------------------------------------------------
CORE RULES:
1. Single Lane: Cars cannot pass each other.
2. Traffic Rule: Faster car catches slower car -> merges into its "fleet"
   and travels at the slower car's speed.
3. Goal: Count total distinct fleets reaching the destination.

=========================================================================
1. OPTIMAL APPROACH: Monotonic Stack (Right-to-Left)
=========================================================================
- Idea: Look at cars from closest to target to furthest away.
- The car closest to the finish line is a fleet leader (no one blocks it).
- Calculate each car's independent ETA: (target - position) / speed.
- Use a stack to track independent fleet ETAs:
  * If a car behind has a SMALLER or EQUAL ETA (stack[-1] <= stack[-2]):
    It crashes into the slower fleet ahead. It merges -> stack.pop().
  * If a car behind has a LARGER ETA:
    It is too slow to catch up. It stays on the stack as a new fleet leader.

Time Complexity:  O(n log n) -> due to sorting positions descending.
Space Complexity: O(n)       -> to store the stack and zipped pairs.
=========================================================================
2. BRUTE FORCE APPROACH (Left-to-Right Simulation)
=========================================================================
- Idea: Sort cars from furthest back to closest to finish.
- Compare each car to the one directly ahead to calculate where/when they crash.
- Problem: "Chain Reaction Merge". If a car ahead merges and slows down, 
  it alters the math for ALL cars driving behind it.
- Requires constantly backtracking and re-evaluating trailing cars.

Time Complexity:  O(n^2) -> updating states backward during cascades.
Space Complexity: O(n)
-------------------------------------------------------------------------
'''
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair and sort: Closest car to finish line first
        cars = sorted(zip(position, speed), reverse = True) # n log n
        stack = []

        for pos, spd in cars:
            # Calculate current cars time to arrivial (ETA).
            current_time = (target - pos) / spd
            stack.append(current_time)

            # If current car is faster the the car infront of it (Smaller current_time (ETA), it joins that fleet.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        # The length of the stack is the ammount of different fleets.
        return len(stack)
