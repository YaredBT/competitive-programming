# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        res, stack, idx = [], [], 0
        while head:
            while stack and stack[-1][0] < head.val:
                _, i = stack.pop()
                res[i] = head.val
            
            res.append(0)
            stack.append((head.val, idx))
            idx += 1
            head = head.next
        return res
