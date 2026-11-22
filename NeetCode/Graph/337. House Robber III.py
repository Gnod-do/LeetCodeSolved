# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def dfs(node):
            if not node:
                return (0, 0)

            L = dfs(node.left)
            R = dfs(node.right)
            rob = node.val + L[1] + R[1]
            skip = max(L) + max(R)

            return (rob, skip)

        return max(dfs(root))