# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def reverseList(self, head):
        pre = None
        curr = head

        while curr:
            nextNode = curr.next
            curr.next = pre
            pre = curr
            curr = nextNode

        return pre

    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        node = self.reverseList(head)

        if not node:
            return None

        if n == 1:
            return self.reverseList(node.next)

        curr = node
        for i in range(1, n - 1):
            if not curr:
                return self.reverseList(node)
            curr = curr.next

        if curr.next:
            removed_node = curr.next
            curr.next = removed_node.next

        return self.reverseList(node)

# Hoac cach don gian hon la tim length cua linked list truoc
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return None

        k = 0

        curr = head
        while curr:
            curr = curr.next
            k += 1

        if k - n == 0:
            return head.next

        curr = head
        for i in range(1, k - n):
            curr = curr.next

        curr.next = curr.next.next

        return head