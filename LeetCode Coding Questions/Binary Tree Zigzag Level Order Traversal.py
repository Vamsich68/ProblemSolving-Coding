# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return root
        que=[]
        res=[]
        que.append(root)
        direction= False
        while que:
            n=len(que)
            temp=[0]*n
            for i in range(n):
                node=que.pop(0)
                if node.left is not None:
                    que.append(node.left)
                if node.right is not None:
                    que.append(node.right)
                if direction:
                    temp[n-1-i]=node.val
                    print(temp[n-1-i],n-1-i)
                else:
                    temp[i]=node.val
            res.append(temp)
            direction = not direction
        return res