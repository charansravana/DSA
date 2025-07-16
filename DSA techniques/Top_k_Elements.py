'''
The Top K Elements pattern involves selecting the K largest or smallest elements from an array. A common and efficient way to approach this is by using a heap (priority queue), especially a min-heap to maintain the top K largest elements. For each element, if it's larger than the smallest in the heap, you replace it, maintaining a running list of top K elements. This gives a time complexity of O(n log k), which is efficient when k is small compared to n.

The "Top K Frequent Elements" problem is a classic use case for the bucket sort pattern, which is ideal when you want to group elements based on their frequency or occurrence count.This pattern is better than brute-force or heap-based approaches in many scenarios because it provides linear time complexity O(n) without additional complexity of maintaining a priority queue or sorting all elements. Since each element appears only once in the map and is added to a bucket at most once, both time and space remain proportional to the input size. The simplicity and efficiency of bucket sort, combined with its intuitive frequency grouping, make it a powerful go-to strategy for frequency-based problems in coding interviews.

Time Complexity: O(n)
Space Complexity: O(n) 

'''

# Leet-code - 347 , Finding Top K Frequent Elements
from collections import Counter
def topKFrequent(self, nums, k):
        freq=Counter(nums)
        n=len(nums)
        buck=[[] for _ in range(n+1)]

        for num,count in freq.items():
            buck[count].append(num)
        
        res=[]

        for i in range(n,0,-1):
            for num in buck[i]:
                res.append(num)
                if len(res)==k:
                    return res  
'''
Time Complexity: O(n)
Space Complexity: O(n) 
'''



# leet-code - 215 , Finding Kth Largest Element in an Array
import heapq
def findKthLargest(self, nums, k) :
        min_heap=nums[:k]
        heapq.heapify(min_heap)

        for num in nums[k:]:
            if num>min_heap[0]:
                heapq.heappushpop(min_heap,num)
        return min_heap[0]

# Time Complexity: O(n log k) for finding Kth largest element
# Space Complexity: O(k) for the min-heap used to store the top K elements
'''
What is heapq?
Python's built-in heapq module provides an implementation of the min-heap.
A heap is a special tree-based structure where the smallest element is always at the root.
In Python, heapq only supports min-heaps by default.

heapify(iterable)
Converts a regular list into a valid min-heap, in-place. After heapify, the smallest element is at index 0.

heappush(heap, item)
Pushes a new element into the heap while maintaining heap order.
heapq.heappush(nums, 0)
print(nums)  # Output: [0, 1, 5, 3, 2]

heappop(heap)
Removes and returns the smallest element from the heap.
smallest = heapq.heappop(nums)
print(smallest)  # Output: 0
print(nums)      # Heap is now re-adjusted

heappushpop(heap, item)
Pushes and pops in one atomic step — more efficient than doing heappush followed by heappop.It pushes item to the heap, then pops and returns the smallest item.
heap = [2, 3, 4]
heapq.heapify(heap)
result = heapq.heappushpop(heap, 1)
print(result)  # Output: 1 (pushed 1, popped 1 immediately — didn't enter heap)
print(heap)    # Heap remains unchanged: [2, 3, 4]


result = heapq.heappushpop(heap, 5)
print(result)  # Output: 2 (pushed 5, then popped 2 — 5 stayed in heap)
print(heap)    # Heap: [3, 5, 4]

Method	    Time Complexity
heapify()	O(n)
heappush()	O(log n)
heappop()	O(log n)
heappushpop()	O(log n)

'''