# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def mirror(a, b):
            if not a and not b:
                return True

            if not a or not b:
                return False

            if a.val != b.val:
                return False

            return mirror(a.left, b.right) and mirror(a.right, b.left)

        if not root:
            return True

        return mirror(root.left, root.right)

