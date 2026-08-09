# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """if p==None and q==None:
            return True
        if p==None or q==None or p.val!=q.val:
            return False
        left=self.isSameTree(p.left,q.left)
        right=self.isSameTree(p.right,q.right)
        return left and right"""
        queue=deque([(p,q)])
        while queue:
            node1,node2=queue.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False          
            if node1.val!=node2.val:
                return False
            queue.append((node1.left,node2.left))
            queue.append((node1.right,node2.right))
        return True
            
        
        