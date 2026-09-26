# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # intuition: perform dfs on root looking for both nodes
        # return the last shared node in the path
        # ancestor can be p or q
        def dfs(root, target, seen): 
            if root is None: 
                return 
            else: 
                seen.append(root)
                if root.val < target:
                    dfs(root.right, target, seen) 
                elif root.val > target: 
                    dfs(root.left, target, seen)
                else:
                    seen.append(root)
        
        p_seen = []
        q_seen = []

        dfs(root, p.val, p_seen)
        dfs(root, q.val, q_seen)

        ancestor = root
        i = 0 
        j = 0
        while i < len(p_seen) and j < len(q_seen):
            if p_seen[i] == q_seen[j]: 
                ancestor = p_seen[i] 
            i += 1 
            j += 1
        return ancestor
