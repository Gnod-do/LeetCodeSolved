# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        pre = None
        current = head

        while current:
            nextNode = current.next
            current.next = pre
            pre = current
            current = nextNode

        return pre

head = [1,2,3,4,5]
sol = Solution()