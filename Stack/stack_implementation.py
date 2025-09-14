class Stack:
    def __init__(self):
        self.items = []   # internal list to store stack elements

    # Push element onto stack
    def push(self, item):
        self.items.append(item)

    # Pop element from stack (removes and returns top)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    # Peek at the top element (without removing it)
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is empty"

    # Check if stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # Get size of stack
    def size(self):
        return len(self.items)



s = Stack()
s.push(10)
s.push(20)
s.push(30)

print(s.peek())  # 30
print(s.pop())   # removes 30
print(s.pop())   # removes 20
print(s.peek())  # 10
