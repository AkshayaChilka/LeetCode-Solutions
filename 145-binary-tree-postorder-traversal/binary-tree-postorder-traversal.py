# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root):
            if root==None:
                return
            helper(root.left)
            helper(root.right)
            l1.append(root.val)
        l1=[]
        helper(root)
        return l1
        