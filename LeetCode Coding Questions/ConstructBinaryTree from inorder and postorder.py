# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree 
and postorder is the postorder traversal of the same tree, construct and return the binary tree.
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) != len(postorder):
            return None
        
        if not inorder:
            return None
        
        root_val = postorder.pop()
        root = TreeNode(root_val)
        
        ind = inorder.index(root_val)
        root.left = self.buildTree(inorder[:ind], postorder[:ind])
        root.right = self.buildTree(inorder[ind+1:], postorder[ind:])
        
        return root
'''
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder)!=len(postorder):
            return None
        if not inorder:
            return None
        root=TreeNode(postorder[len(postorder)-1])
        ind= inorder.index(postorder[len(postorder)-1])
        root.left=self.buildTree(inorder[:ind],postorder[:ind])
        root.right = self.buildTree(inorder[ind+1:],postorder[ind:-1])
        return root
