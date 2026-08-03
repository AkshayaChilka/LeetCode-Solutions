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
        st=[]
        curr=root
        ans=[]
        while(curr!=None or st!=[]):
            while(curr!=None):
                st.append(curr)
                curr=curr.left
            node=st.pop()
            ans.append(node.val)
            curr=node.right
        return ans



        