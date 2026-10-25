"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return None

        old_to_new = {node: Node(node.val)}

        stack = [node]

        while stack:
            u = stack.pop()

            for neighbor in u.neighbors:
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)

                old_to_new[u].neighbors.append(old_to_new[neighbor])

        return old_to_new[node]