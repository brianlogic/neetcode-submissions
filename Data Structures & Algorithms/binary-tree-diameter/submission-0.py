# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = 0 

        def dfs(root):
            # base case none 
            nonlocal diameter 
            
            if root is None:
                return 0 
            else: 
                # in normal height/ depth we could just take the max of the left and right node
                # however, now we have to include in our calculation the left + right
                # but we can't include that in our max because it'll recurse that pathway upwards to a node 
                # we need to handle the split calculations 
                left = dfs(root.left)
                right = dfs(root.right)

                diameter = max(diameter, left + right)
                return 1 + max(left, right) # basically normal depth - 1

        dfs(root)
        return diameter 