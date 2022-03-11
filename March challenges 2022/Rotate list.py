# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        temp = head
        count = 1
        while(temp.next!=None):
            count+=1
            temp = temp.next
            
            
        temp.next = head
        t = count-k%count-1
        
        temp = head
        while(t>0):
            temp = temp.next
            t-=1
        head = temp.next
        temp.next = None
        
        return head