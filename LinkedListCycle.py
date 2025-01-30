

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        #brute force - Uses a hash set

        """ seen = set()
        curr = head

        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next
        return False """

        #optimal solution

        


        