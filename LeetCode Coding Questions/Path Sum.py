class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfsSum(node,currentsum):
            if not node:
                return False
            currentsum+=node.val
            if not node.left and not node.right :
                return currentsum==targetSum
            return (dfsSum(node.left,currentsum) or dfsSum(node.right, currentsum))
        return dfsSum(root,0)