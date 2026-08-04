# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """def helper(node, low, high):
            if node==None:
                return True
            if node.val <= low or node.val >= high:
                return False
            return (helper(node.left, low, node.val) and
                    helper(node.right, node.val, high))
        return helper(root, float("-inf"), float("inf"))"""
        def inorder(root):
            if root==None:
                return
            inorder(root.left)
            l1.append(root.val)
            inorder(root.right)
        l1=[]
        inorder(root)
        for i in range(1,len(l1)):
            if l1[i]<=l1[i-1]:
                return False
        return True


        


        
        