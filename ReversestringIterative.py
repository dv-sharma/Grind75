# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        currentNode=head
        previous=None

        while currentNode:
            next_tmp_node=currentNode.next
            currentNode.next=previous
            previous=currentNode
            currentNode=next_tmp_node

        return previous
            
'''

PREVIOUS    CURRENT->  CURRENT.NEXT - NONE(TAIL)
Store the next in temp,
Current.next will point to previous
Previous will move forward to current node
and current takes the next temp value to mantain the iteration

'''
##########ITERATIVE
if head is None or head.next == None:
            return head

        reversedhead= self.reverseList(head.next)
        head.next.next=head
        head.next=None

        return reversedhead






        
