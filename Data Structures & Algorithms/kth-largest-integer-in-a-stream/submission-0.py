import heapq

class KthLargest:
    '''
    Time: O(N)
    Space: O(log k)
    '''

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap) # O(N)

        while len(self.min_heap) > self.k: # O((N - k)log N)
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]
