# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import heappush, heappop, heapreplace, heapify
class Solution:
    # Idea: store all list heads in a heap as tuples of (value, id, node) [note: id only needed for heap comparisons]
    # As you add each node to the resulting list, pop it from the heap, or
    # replace it with its next node if it exists
    # Complexity: Time O(nklogk) Space O(k), where n is the length of the longest linked list, k is the number of lists
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        newHead = ListNode(-1)
        newHeadTemp = newHead
        h = []
        for node in lists:
            if node:
                h.append((node.val, id(node), node))
        heapify(h)
        while len(h):
            newHeadTemp.next = h[0][2]
            newHeadTemp = newHeadTemp.next
            if newHeadTemp.next:
                heapreplace(h, (newHeadTemp.next.val, id(newHeadTemp), newHeadTemp.next))
            else:
                heappop(h)
        return newHead.next

# Alternative divide and conquer recursion approach
# Same time complexity as above
class Solution:
    # Can do the merge 2 lists iteratively or recursively
    def merge2Lists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            list1.next = self.merge2Lists(list1.next, list2)
            return list1
        else:
            list2.next = self.merge2Lists(list1, list2.next)
            return list2

    def merge2Lists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        newHead = newHeadTemp = ListNode(-1)
        while list1 and list2:
            if list1.val < list2.val:
                newHeadTemp.next = list1
                list1 = list1.next
            else:
                newHeadTemp.next = list2
                list2 = list2.next
            newHeadTemp = newHeadTemp.next
        if list1:
            newHeadTemp.next = list1
        else:
            newHeadTemp.next = list2
        return newHead.next
        
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return self.merge2Lists(lists[0], lists[1])
        return self.merge2Lists(self.mergeKLists(lists[:len(lists)//2]), self.mergeKLists(lists[len(lists)//2:]))