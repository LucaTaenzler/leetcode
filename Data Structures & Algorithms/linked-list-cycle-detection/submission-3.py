# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l, r = head, head

        while l and r:
            if l.next:
                l = l.next
            else:
                return False

            if r.next:
                r = r.next
            else:
                return False
            if r.next:
                r = r.next
            else:
                return False

            if l == r:
                return True

        return False