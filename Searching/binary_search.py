'''
Binary Search Algorithm is a searching algorithm used in a sorted array by repeatedly dividing the search interval in half. The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(log N). 

Conditions to apply Binary Search Algorithm in a Data Structure :

-> The data structure must be sorted.
-> Access to any element of the data structure should take constant time.

Binary Search Algorithm Steps:

Binary search efficiently finds a target value in a sorted array by repeatedly dividing the search range in half. You start with two pointers: one at the beginning (low) and one at the end (high) of the array. Then:

Calculate the middle index: mid = (low + high) // 2.
Compare the middle element with the target:
    If they are equal, return mid.
    If the target is less, update high = mid - 1 to search the left half.
    If the target is greater, update low = mid + 1 to search the right half.
Repeat steps 1-2 until the target is found or the search range is empty (low > high).
If not found, return -1.

The Binary Search Algorithm can be implemented in the following two ways

1.Iterative Binary Search Algorithm
2.Recursive Binary Search Algorithm

Time Complexity: 
Best Case: O(1)
Average Case: O(log N)
Worst Case: O(log N)

Auxiliary Space: O(1), If the recursive call stack is considered then the auxiliary space will be O(log N).

'''

# 1.Iterative Binary Search Algorithm
def binary_search(arr, target):
    left=0
    right=len(arr)-1
    while (left<=right):
        mid = (left + right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left = mid+1
        else:
            right=mid-1
    return -1   

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_value = 7
print(binary_search(my_list, target_value))  # Output: 6 (index of the target value)


# 2.Recursive Binary Search Algorithm
def binarySearch(arr, low, high, x):
    if high >= low:
        mid = low + (high - low) // 2
        
        if arr[mid] == x:
            return mid
        # If element is smaller than mid, then it
        # can only be present in left sub-array
        elif arr[mid] > x:
            return binarySearch(arr, low, mid-1, x)
        # Else the element can only be present
        # in right sub-array
        else:
            return binarySearch(arr, mid + 1, high, x)
    else:
        return -1

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_value = 4
print(binarySearch(my_list, 0, len(my_list)-1, target_value))

# Binary Search on 2D Array
"""
    Searches for a target value in a 2D array that is sorted
    both row-wise and column-wise.

    Args:
        matrix: A list of lists (2D array) of integers.
        target: The integer value to search for.

    Returns:
        A tuple (row, col) of the target's index if found,
        otherwise returns (-1, -1).
"""

def search_in_2d_array(matrix, target):
    if not matrix or not matrix[0]:
        return (-1, -1)  # Handle empty matrix

    rows = len(matrix)
    cols = len(matrix[0])

    # Start from the top-right corner
    row = 0
    col = cols - 1

    while row < rows and col >= 0:
        current_element = matrix[row][col]

        if current_element == target:
            return (row, col)  
        elif current_element > target:
            col -= 1  # Move left
        else:
            row += 1  # Move down

    return (-1, -1) 


sorted_matrix = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [27, 29, 37, 48],
    [32, 33, 39, 50]
]

target_value = 29
result = search_in_2d_array(sorted_matrix, target_value)
print(f"Target {target_value} found at index: {result}")  # Output: Target 29 found at index: (2, 1)


'''
Time Complexity: O(m+n)
The time complexity is O(m+n), where m is the number of rows and n is the number of columns.

Space Complexity: O(1)
The space complexity is O(1) since we are using a constant amount of extra space.
'''


'''
Pre-computation Required: Binary search and two-pointer techniques fail on unsorted data. You must sort the array first.
Sorting Cost: Efficient sorting takes O(nlogn).
Total Complexity on Unsorted Data: The total time becomes O(nlogn) because sorting is the bottleneck.
Single Search Rule: For a one-time search on an unsorted array, a simple Linear Search (O(n)) is faster than sorting and then searching (O(nlogn)).
'''

