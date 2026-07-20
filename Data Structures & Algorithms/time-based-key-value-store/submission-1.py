class TimeMap:
    def __init__(self):
        '''
        Total Space Complexity: O(m * n)
        - m accounts for the total amount of unique keys.
        - n accounts for the average or maximum length of each keys value array.

        Time Complexity: O(1)
        '''

        # Creates the Hash Map used to store the key, value pairs.
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        '''
        Time Complexity: O(1)
        '''

        # Add key to map along with its own array if not already in the map.
        if key not in self.time_map:
            self.time_map[key] = []
        
        # Appends the [timestamp : value] pair to the value array for the key.
        self.time_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        '''
        Time Complexity: O(log n)
        '''
        res = ""

        # Creates the values list for the key we are working on.
        values = self.time_map.get(key, [])

        # We use Binary Search since our timestamps are in increasing order.
        left, right = 0, len(values) - 1
        while left <= right:
            mid = left + (right - left) // 2

            # If current time is <= timestamp it is valid, so we move our left pointer inward in hopes of finding an even greater valid time.
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                left = mid + 1

            # Otherwise we move the right pointer inward in hopes of finding a smaller valid time.
            else:
                right = mid - 1
        
        # Eventually the pointers cross and we return our result string.
        return res
    
