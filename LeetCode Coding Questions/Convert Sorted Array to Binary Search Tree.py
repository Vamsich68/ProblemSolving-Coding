# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def bst(a,b):
            if a>b:
                return None
            mid = (a+b)//2
            root = TreeNode(nums[mid])
            root.left = bst(a,mid-1)
            root.right = bst(mid+1,b)
            return root
        return bst(0,len(nums)-1)