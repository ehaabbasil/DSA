# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize Pointers
        prev = None # Previous Node starts as None
        curr = head  # Current node start at the head 

        # Traverse the list 
        while curr is not None:
            next_node = curr.next # save the next node

            curr.next = prev  # reverse the link

            # Move pointers forward
            prev = curr    # Move prev to the current node
            curr = next_node  # Move curr to the next node
        # prev is now the new head of the reversed list  
        return prev
        



