class Solution:
    '''
        Time: O(n)
        Space: O(1)
    '''
    def isPalindrome(self, s: str) -> bool:
        # Our two pointers to track both ends of s.
        left, right = 0, len(s) - 1

        while left < right:

            # If we hit an invalid character move the pointers up.
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            # If the valid characters are not equal then return False.
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
'''
    Brute Force Approach: We can take the string and remove all non alpha numeric characters
    and call it a clean string. Then we take that clean string and reverse it.
    We then compare the two strings created and see if they match. If they match then we found
    a palindrome.
        Time: O(n)
        Space: O(n) - Since we must allocate extra memory to store the cleaned
                      and reversed versions of the string.
'''