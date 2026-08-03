# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """l1=[]
        def helper(root):
            if root==None:
                return
            if root!=None:
                l1.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        return l1"""
        if root==None:
            return []
        st=[root]
        ans=[]
        curr=root
        while(st!=[]):
            node=st.pop()
            ans.append(node.val)
            if node.right!=None:
                st.append(node.right)
            if node.left!=None:
                st.append(node.left)
        return ans
        