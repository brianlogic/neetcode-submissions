"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashmap = {}
        def cloneHelper(node): 
            if node is None: # case 1 node is none, we prob won't have this case
                return None
            elif len(node.neighbors) == 0: # case where a node is disconnected
                return Node(node.val, None)
            else: # case 3 neighbors present, perform a recursive call on them
            # use a dictionary so we don't create a bunch of duplicates
                new_node = Node(node.val, None)
                hashmap[new_node.val] = new_node
                for neighbor in node.neighbors: 
                    if neighbor.val in hashmap: # neighbor already seen
                        new_node.neighbors.append(hashmap[neighbor.val])
                    else: # neighbor not seen 
                        new_node.neighbors.append(cloneHelper(neighbor))
                return new_node
        return cloneHelper(node)
            