"""
23. Merge k Sorted Lists [Hard]

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

"""

import heapq

def mergeKLists(lists):

    minHeap = []

    for i, node in enumerate(lists):
        if node:
            heapq.heappush(minHeap, (node.val, i, node))

    dummy = ListNode(0)
    tail = dummy

    while minHeap:
        val, i, node = heapq.heappop(minHeap)
        tail.next = node
        tail = tail.next

        if node.next:
            heapq.heappush(minHeap, (node.next.val, i, node.next))

    return dummy.next
