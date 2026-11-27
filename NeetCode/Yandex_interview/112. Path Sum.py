def hasPathSum(root, targetSum):
    if not root:
        return False

    if not root.left and not root.right:
        return root.val == targetSum

    remain = targetSum - root.val
    return hasPathSum(root.left, remain) or hasPathSum(root.right, remain)

