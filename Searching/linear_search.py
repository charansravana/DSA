''' 
What is Linear Search 
Linear search, also known as sequential search, is a simple searching algorithm used to find a specific element in a list or array. It works by checking each element in the list one by one, starting from the beginning and continuing until it either finds the target value or reaches the end of the list.

How Linear Search Works
Start at the first element of the list Compare the target value to the current element,If the current element matches the target, return its position (index).If it doesn't match, move to the next element,Continue this process until the element is found or the list ends.
If the target is not found by the end, the algorithm returns that the value is absent.

Case	    Time Complexity	Explanation
Best Case	    O(1)	    The target value is at the first element.
Average Case	O(n)	    The target is somewhere in the middle, or not present at all.
Worst Case	    O(n)	    The target is at the last element or not present in the 
                            array/list.

Space Complexity :- O(1) (No extra space is used—just a variable for the index and possible return)

When to choose linear search:

=> When the data is unsorted (it works on any order).
=> For small lists (usually less than a few hundred elements).
=> When the data changes frequently (adding or deleting elements).
=> If you want a simple and quick-to-implement solution.
=> When you do infrequent searches and don’t want the overhead of sorting or more complex methods.
=> When using data structures with only sequential access like linked lists

'''

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# Example usage:
my_list = [3, 7, 2, 9, 5, 1, 8, 4, 6]
target_value = 4
print(linear_search(my_list, target_value))  # Output: 7 (index of the target value)

