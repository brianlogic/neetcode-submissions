# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # first build proper list based on height 

        def getHeight(root): 
            if root is None:
                return 0 
            else: 
                return 1 + max(getHeight(root.left), getHeight(root.right))
        
        length = getHeight(root)
        result = [[] for _ in range(length)] 
        

        # during recursive calls, we track what height we're at so we know where to insert a value into the list 
        def helper(root, i):
            if i == length or root is None: 
                return 
            else: # root is defined
                result[i].append(root.val)
                helper(root.left, i + 1)
                helper(root.right, i + 1)
        helper(root, 0)
        return result 