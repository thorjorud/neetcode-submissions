class TimeMap:
    """
    Total Space Complexity: O(M * N)
        - M is the total number of UNIQUE KEYS in our hashmap.
        - N is the average or maximum number of [timestamp, value] pairs stored per key.
    """
    def __init__(self):
        '''
        Time Complexity: O(1)
        '''
        # We use a hashmap to store the keys along with an array
        # to store the timestamp and values.
        # This allows us O(1) lookup speed.
        # EX: {"bob" : [2, "happy"]}
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        '''
        Time Complexity: O(1)
        '''
        # If key is not in our map, then add it to the map with a fresh array as the value.
        if key not in self.store:
            self.store[key] = []

        # Appending to a list and inserting into a hashmap run in O(1) time.
        # Since each time we add must be > all previous times we know
        # the timestamps will be in ascending order in our value array.
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        '''
        Time Complexity: O(log n)
        '''
        res = ""

        # Gather the values array which stores all our [timestamp : value] pairs.
        # Since the timestamps are sorted we can use Binary Search.
        values = self.store.get(key, [])

        left, right = 0, len(values) - 1

        while left <= right:
            mid = (left + right) // 2

            # If current mid time is <= to the request timestamp then it is a valid time!
            # We store this pairs value in our res list. If we find another
            # valid time that comes later then we will just update res.
            # We then move the left pointer to the right half of the search space,
            # In hopes of finding a larger valid time.
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                left = mid + 1
            
            # Otherwise if current mid time is > then the requested timestamp.
            # That means we must search the left half of the search space.
            # We move the right pointer in hopes of finding a smaller time.
            else:
                right = mid - 1

        # Once the pointers cross, we return the res string.
        return res
