# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """def helper(root):
            if root==None:
                return
            helper(root.left)
            l1.append(root.val)
            helper(root.right)

        l1=[]
        helper(root)
        return l1"""
        stack=[]
        result=[]
        curr=root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            result.append(curr.val)
            curr=curr.right
        return result

        



        