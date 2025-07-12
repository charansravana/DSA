'''
In-place reversal of a linked list
In-place reversal of a linked list refers to the process of reversing the order of the nodes in a linked list without using additional data structures to store the elements. This means that the modification is done by directly manipulating the pointers within the existing linked list structure, making it memory-efficient. 

Complexity analysis
Time Complexity: O(n), where 'n' is the number of nodes in the linked list. Each node is visited and its pointer is modified once.
Space Complexity: O(1), as it uses only a few pointers for auxiliary storage, regardless of the size of the linked list.

leet-code - 206,92,24

'''

#leet-code : 206
def reverseList(self, head):
    prev = None
    crnt = head
    while crnt != None:
        nxt = crnt.next
        crnt.next=prev
        prev=crnt
        crnt = nxt
    return prev

#leet-code : 92
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverseBetween(self, head, left, right) :
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        current = prev.next
        for _ in range(right - left):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next