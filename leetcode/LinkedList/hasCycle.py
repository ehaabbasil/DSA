# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # #Brute Force 
        # # T O(n) : S O(n)
        # cur = head
        # visited = set() 

        # while cur:
        #     if cur in visited:
        #         return True 
        #     visited.add(cur)
        #     cur = cur.next
        # return False

        #Floyd's Tortoise and Hare
        # Time O(n) Space: O(1)
        fast = slow = head 

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
            
            if slow == fast:
                return True 
        return False
        