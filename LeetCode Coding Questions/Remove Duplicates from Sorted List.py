# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        while(current!=None):
            if current.next and current.val==current.next.val:
                current.next=current.next.next
            else:
                current=current.next
        return head
lst=[1,2,3,3,4,4,5]
head=ListNode(lst[0])
listnode=head
for i in range(1,len(lst)):
    listnode.next=ListNode(lst[i])
    listnode=listnode.next
solution=Solution()
res=solution.deleteDuplicates(head)
while res:
    print(res.val)
    res=res.next