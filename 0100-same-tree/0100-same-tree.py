# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        tree1 = []
        tree2 = []
        def preorder(res,root):
            if not root:
                res.append('#')
                return
            res.append(str(root.val))
            preorder(res,root.left)
            preorder(res,root.right)
            
        preorder(tree1,p)
        preorder(tree2,q)
        return tree1 == tree2