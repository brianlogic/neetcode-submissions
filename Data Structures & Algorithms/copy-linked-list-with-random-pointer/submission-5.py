"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # we can use a hashmap to keep references aligned

        # the .next value is easy
        hashmap = {} 

        cur = head

        while cur: 
            hashmap[cur] = Node(cur.val, None, None)
            cur = cur.next

        cur = head
        while cur:
            hashmap[cur].next = hashmap[cur.next] if cur.next else None
            hashmap[cur].random = hashmap[cur.random] if cur.random else None
            cur = cur.next

        return hashmap[head] if head else None