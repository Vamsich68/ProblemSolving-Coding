# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return root
        que=[]
        res=[]
        que.append(root)
        while que:
            temp=[]
            n=len(que)
            for i in range(n):
                node=que.pop(0)
                temp.append(node.val)
                if node.left is not None:
                    que.append(node.left)
                if node.right is not None:
                    que.append(node.right)
            res.append(temp)
        return res

