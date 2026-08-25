# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        c=head
        length=0
        while c:
            length+=1
            c=c.next

        res=ListNode()
        curr=res
        node=head
        i=0


        while node:
            if i==(length-n):
                if node.next:
                    node=node.next
                else:
                    curr.next=None
                    break
            curr.next=node
            node=node.next
            curr=curr.next
            i+=1
                    
        return res.next

        