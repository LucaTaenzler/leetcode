# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        l1 = list1
        l2 = list2
        start = result = ListNode()

        while l1 and l2:
            if l1.val > l2.val:
                result.next = l2
                l2 = l2.next
            else:
                result.next = l1
                l1 = l1.next
            result = result.next

        result.next = l1 or l2

        return start.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists or lists[0] is None:
            return None

        for i in range(1, len(lists)):
            lists[i] = self.mergeTwoLists(lists[i], lists[i - 1])
        
        return lists[len(lists) - 1]