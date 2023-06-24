# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current, previous = head, None
        while current :
            temp = current.next
            current.next = previous
            previous = current
            current = temp
            #print(previous.val)
        return previous
lst=[1,2,3,3,4,4,5]
head=ListNode(lst[0])
listnode=head
for i in range(1,len(lst)):
    listnode.next=ListNode(lst[i])
    listnode=listnode.next
solution=Solution()
res=solution.reverseList(head)
'''
while res:
    print(res.val)
    res=res.next
    '''