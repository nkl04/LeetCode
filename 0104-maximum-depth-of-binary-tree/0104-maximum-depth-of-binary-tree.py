# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def maxSubDepth(root):
            depth = 0
            if not root:
                return 0
            depth += 1
            return depth + max(maxSubDepth(root.left),maxSubDepth(root.right))
        
        return maxSubDepth(root)