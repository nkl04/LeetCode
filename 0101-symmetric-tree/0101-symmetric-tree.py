# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def preorder(sub,root):
            if not root:
                sub.append('#')
                return
            sub.append(root.val)
            preorder(sub,root.left)
            preorder(sub,root.right)
        def postorder(sub,root):
            if not root:
                sub.append('#')
                return
            sub.append(root.val)
            postorder(sub,root.right)
            postorder(sub,root.left)
        
        left_sub, right_sub = [],[]
        preorder(left_sub,root.left)
        postorder(right_sub,root.right)
        return left_sub == right_sub
