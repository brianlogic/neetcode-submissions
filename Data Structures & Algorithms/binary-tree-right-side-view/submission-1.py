# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # prioritize right side elements
        # we could solve by creating level order traversal and selecting [-1] from each level
        result = [] 
        def helper(root, i): 
            if root is None: 
                return 
            else: 
                if len(result) <= i: 
                    result.append(root.val)
                helper(root.right, i + 1)
                helper(root.left, i + 1)
        helper(root, 0)
        return result 
        
        