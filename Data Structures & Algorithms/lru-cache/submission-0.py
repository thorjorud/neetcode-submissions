class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    '''
    Time Complexity: O(1)
    Space Complexity: O(n)
        - Hashmap and Doubly Linked List grow in direct proportion with cache max capacity.
    '''
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # {key : node}

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        # Connect both dummy nodes initially since linked list is empty.
        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node):
        # Detaches old node.
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _insert(self, node):
        # Two nodes we are going to insert in between.
        prev = self.right.prev
        nxt = self.right

        prev.next = node # Tells current last node to point to new node.
        nxt.prev = node # Tells right dummy node to point back to new node.
        node.prev = prev # Tells new node to point back to prev.
        node.next = nxt # Tells new node to point forward to dummy right node.

    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key]) # Remove node from old spot
            self._insert(self.cache[key]) # Insert node to the far right before dummy.
            return self.cache[key].val # Return the actual value.
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove old version of node if in the cache.
            self._remove(self.cache[key])
        
        # Add new node to cache with new val.
        self.cache[key] = Node(key, value)
        # Insert new node into linked list.
        self._insert(self.cache[key])

        # If cache size grows to large.
        if len(self.cache) > self.capacity:
            # LRU = least recentley used node
            lru = self.left.next
            # Remove from linked list and cache hash map.
            self._remove(lru)
            del self.cache[lru.key]