# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def recurse(node, maximum): 
            if not node:
                return 0
            else: 
                good = 0
                if node.val >= maximum:
                    good = 1
                return good + recurse(node.left, max(maximum, node.val)) + recurse(node.right, max(maximum, node.val))
                
        
        return recurse(root, float("-inf"))