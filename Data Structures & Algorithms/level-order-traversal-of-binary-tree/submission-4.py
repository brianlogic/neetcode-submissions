# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = [] 
        def helper(root, i):
            if root is None: 
                return 
            else:
                if len(result) <= i: 
                    result.append([])
                result[i].append(root.val)
                helper(root.left, i + 1)
                helper(root.right, i + 1)
        helper(root, 0)
        return result 