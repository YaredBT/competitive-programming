# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        curr = head
        while curr.next != None:
            if curr.val == curr.next.val:
                tmp = curr.next
                curr.next = curr.next.next
                del tmp
            else:
                curr = curr.next
        return head     
