'''
The "fast and slow pointers" or "tortoise and hare" pattern is a common technique in algorithm design, particularly useful for solving problems related to linked lists and arrays. It involves using two pointers that traverse a data structure at different speeds. Typically, one pointer (the "slow" pointer) moves one step at a time, while the other (the "fast" pointer) moves two steps at a time. This pattern is particularly helpful for detecting cycles and finding the middle of a linked list.

How it works:
Cycle Detection:
If a data structure (like a linked list) contains a cycle, the fast pointer will eventually "catch up" to the slow pointer, indicating the presence of a cycle. This is analogous to two runners on a circular track, where the faster runner will inevitably overtake the slower one if the track is circular. 
Finding the Middle:
When there's no cycle, the fast pointer will reach the end of the data structure first. At that point, the slow pointer will be at the middle of the structure. 

Common Applications:
Cycle Detection in Linked Lists: The most common application is to detect if a linked list has a cycle (a loop where a node points back to a previous node). 
Finding the Middle of a Linked List: Determining the middle node of a linked list is another frequent use case. 
Other Problems: The fast and slow pointers pattern can also be applied to other problems, such as finding the kth node from the end of a linked list or detecting duplicate elements in an array. 

Time and Space Complexity:
The time complexity of algorithms using the fast and slow pointers is generally O(n), where n is the number of elements in the data structure. The space complexity is O(1) since only a constant amount of extra space is used for the two pointers.

Leet-code Problems: 876 , 141 , 202 , 287
'''

#Leet-code Problem: 876 [middle element]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head:ListNode) -> ListNode:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow

# Leet-code Problem: 141 [cycle detection]
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                return True
        return False 
    
# Leet-code Problem: 202 [happy number]
class Solution:
    def getNext(self, n: int) -> int:
        total_sum = 0
        while n > 0:
            d = n % 10
            n = n // 10
            total_sum += d * d
        return total_sum
    
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.getNext(n)
        
        while fast != 1 and slow != fast:
            slow = self.getNext(slow)
            fast = self.getNext(self.getNext(fast))
        
        return fast == 1