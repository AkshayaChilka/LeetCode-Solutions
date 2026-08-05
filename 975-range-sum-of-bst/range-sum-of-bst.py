# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        l1=[]
        def helper(root):
            if root==None:
                return []
            helper(root.left)
            l1.append(root.val)
            helper(root.right)
        l1=[]
        helper(root)
        ans=0
        for i in range(len(l1)):
            if low <= l1[i] <= high:
                ans+=l1[i]
            
        return ans



        


        