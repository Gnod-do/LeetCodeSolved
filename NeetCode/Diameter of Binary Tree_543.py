# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.res = 0

        #return height
        def dfs(currNode):
            if not currNode:
                return 0

            left = dfs(currNode.left)
            right = dfs(currNode.right)

            self.res = max(self.res, left + right)
            return max(left, right) + 1

        dfs(root)
        return self.res
