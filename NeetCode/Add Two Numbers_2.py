# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = None
        curr = None
        carry = 0

        head1 = l1
        head2 = l2

        while head1 or head2 or carry != 0:
            sumVal = carry

            if head1:
                sumVal += head1.val
                head1 = head1.next

            if head2:
                sumVal += head2.val
                head2 = head2.next

            newNode = ListNode(sumVal % 10)
            carry = sumVal // 10

            if res is None:
                res = newNode
                curr = newNode
            else:
                curr.next = newNode
                curr = curr.next

        return res