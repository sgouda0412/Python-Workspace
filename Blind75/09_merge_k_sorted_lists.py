# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional, ListNode, List
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []

        for i, l in enumerate(lists):
            if l:
                heapq.heappush(h, (l.val,i))

        dummy, curr = ListNode(0)

        while h:
            i, val = heapq.heappop(h)
            curr.next = ListNode(val)
            if lists[i].next:
                heapq.heappush(h, (lists[i].next.val, i))
                lists[i] = lists[i].next
            curr = curr.next
        
        return dummy.next
    
        #==========================================================================
        min_heap = []
        dummy_node = ListNode(-1)

        for node in lists:
            while node:
                heapq.heappush(min_heap, node.val)
                node = node.next
        curr = dummy_node
        while min_heap:
            new_node = ListNode(heapq.heappop(min_heap))
            curr.next = new_node
            curr = curr.next

        return dummy_node.next

        #==========================================================================