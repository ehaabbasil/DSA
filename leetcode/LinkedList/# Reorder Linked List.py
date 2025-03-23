# Reorder Linked List 

# find the second half of linked list 
# reverse the second half 
# merge the 1st half with second half ==> ans 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head:
            return


        slow = fast = head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None 
        cur = slow 

        while cur:
            cur.next, prev, cur = prev, cur, cur.next

        first = head 
        second = prev 


        while second.next:
            first.next, first = second, first.next
            second.next,second = first, second.next

        
        