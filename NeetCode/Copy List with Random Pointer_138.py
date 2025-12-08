"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from lib2to3.pytree import Node


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        mp = {}

        curr = head
        while curr:
            mp[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            nextNode = mp.get(curr)
            nextNode.next = mp.get(curr.next)
            nextNode.random = mp.get(curr.random)
            curr = curr.next

        return mp.get(head)
