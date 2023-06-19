# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        current, previous = head, dummy
        while current:
            while current.next and current.val == current.next.val:
                current=current.next
            if previous.next==current:
                previous = previous.next
                current = current.next
            else:
                previous.next = current.next
                current = previous.next
        return dummy.next