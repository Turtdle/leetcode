def maxDepth(root: Optional[TreeNode]):
    return max(maxDepth(root.left), maxDepth(root.right)) + 1 if root else 0