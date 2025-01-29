# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        
        #Avoid the edge case of having an initial empty list

        #create a copy of the dummy node to work with
        dummy = node = ListNode() # type: ignore

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1       #list1 node itself
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next        # move forward in the new list
        
        if list1:
            node.next = list1
        else:
            node.next = list2

        #node.next would refer to the next node in the list (which in this case could be None), not the head of the list. 
        #So, we return dummy.next to get the first real node of the merged list.
        return dummy.next

