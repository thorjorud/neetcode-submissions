'''
Time Complexity: O(m)
Space Complexity: O(m)
'''

class Solution:
    # Wrapper, creates our encoded string in this format: f'{len(s)}#{s}' (e.g. 4#Hello).
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += f"{len(s)}#{s}"
        return encoded_str

    # Unwrapper, takes the encoded str and converts back into an array of strs.
    def decode(self, s: str) -> List[str]:
        res = []
        # Main pointer
        i = 0
        while i < len(s):
            # Temp pointer used to locate the '#'.
            j = i
            while s[j] != "#":
                j += 1

            # Finds length of str and stores it as an int.
            length = int(s[i:j])

            # Finds beginning and ending indices of current str.
            start_of_str = j + 1
            end_of_str = start_of_str + length

            res.append(s[start_of_str:end_of_str])

            # Set our main pointer to the end of the last word covered.
            i = end_of_str
            
        return res