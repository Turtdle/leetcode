def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    output = [] 
    if not root: return output

    stack = []
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        output.append(current.val)
        current = current.right
    return output

