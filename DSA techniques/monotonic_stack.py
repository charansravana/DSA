'''
A monotonic stack is a special data structure used in algorithmic problem-solving. Monotonic Stack maintaining elements in either increasing or decreasing order. It is commonly used to efficiently solve problems such as finding the next greater or smaller element in an array etc.
                                            (or)

A Monotonic Stack is a common data structure in computer science that maintains its elements in a specific order. Unlike traditional stacks, Monotonic Stacks ensure that elements inside the stack are arranged in an increasing or decreasing order based on their arrival time. In order to achieve the monotonic stacks, we have to enforce the push and pop operation depending on whether we want a monotonic increasing stack or monotonic decreasing stack.


'''

#monotonic decreasing stack (You pop smaller values to find the next greater)

def next_greater_element(arr):
    stack=[]
    result = [-1] * len(arr)
    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            index= stack.pop()
            result[index]=arr[i]
        stack.append(i)

    return result
arr=[1, 3, 2, 4]
print(next_greater_element(arr))  # Output: [3, 4, 4, -1]

'''
Time and space Complexity :
Monotonic Stack	: - 
        Time complexity  : O(n)	
        Space complexity : O(n)
Brute-force	
        Time complexity  : O(n^2)	
        Space complexity : O(1)	
'''

#monotonic increasing stack (You pop greater values to find the next smaller)

def next_smaller_element(arr):
    stack=[]
    result = [-1] * len(arr)
    for i in range(len(arr)):
        while stack and arr[i] < arr[stack[-1]]:
            index= stack.pop()
            result[index]=arr[i]
        stack.append(i)

    return result
arr=[1, 3, 2, 4]
print(next_smaller_element(arr))  

'''
Time and space Complexity :
Monotonic Stack	: - 
        Time complexity  : O(n)	
        Space complexity : O(n)
Brute-force	
        Time complexity  : O(n^2)	
        Space complexity : O(1)	
'''
