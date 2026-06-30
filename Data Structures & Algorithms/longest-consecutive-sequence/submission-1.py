class Solution:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    Brute Force Approach:
    - Concept: Treat every number in the array as a potential starting point. For each 
      number, scan the rest of the array for num + 1, num + 2, etc., using a loop.
    - Time Complexity: O(n^2) or O(n^3) because searching the array takes O(n) time, 
      and we repeat this search for multiple numbers in a sequence.
    - Space Complexity: O(1) as no extra data structures are used.

    Optimized Approach (Below):
    - Concept: Trade space for time by dumping all numbers into a Hash Set, turning 
      lookups into instant O(1) operations. To prevent redundant work, we only build 
      a sequence if the current number is the absolute START of that sequence 
      (i.e., 'num - 1' does not exist in the set).

    Why the Nested Loops are strictly O(n) Time:
    An interviewer might see a 'while' loop inside a 'for' loop and assume O(n^2), 
    but this solution is strictly linear due to the "At-Most-Twice" Lookup Rule:
    
    1. The First Lookup (The 'if' check): The main 'for' loop inspects every number 
       exactly once to check if its left-neighbor (num - 1) exists. If it does, the 
       number is instantly skipped.
    2. The Second Lookup (The 'while' loop): A number is only looked at a second time 
       if it is part of an ongoing chain being counted by a valid sequence starter.

    Because middle and end numbers are blocked from ever starting a new chain, each 
    consecutive sequence is built exactly once. Since no element in the dataset can 
    be touched more than twice, the total operations are capped at 2n, which 
    simplifies perfectly to O(n) time.
    """
    def longestConsecutive(self, nums: List[int]) -> int:

        # Dump all numbers into a set for O(1) lookups.
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:

            # If num is the start of a streak. (Meaning a number smaller by one doesnt exist in the set)
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1

                # While streak is still valid.
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1

                # Update longest streak.
                longest_streak = max(longest_streak, current_streak)

        return longest_streak