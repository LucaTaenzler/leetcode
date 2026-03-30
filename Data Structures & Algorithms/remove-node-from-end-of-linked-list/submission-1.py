# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        counter = head
        while counter:
            length += 1
            counter = counter.next

        from_front = length - n
        first = head
        second = dummy = ListNode(0, head)

        for n in range(from_front):
            second = second.next

        second.next = second.next.next

        return dummy.next