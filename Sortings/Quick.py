''' 
QuickSort is a sorting algorithm based on the Divide and Conquer that picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array. It works on the principle of divide and conquer, breaking down the problem into smaller sub-problems.

To implement the Quicksort algorithm, we need:

A quickSort method that calls itself (recursion) if the sub-array has a size larger than 1.
A partition method that receives a sub-array, moves values around, swaps the pivot element  into the sub-array and returns the index where the next split in sub-arrays happens.

Time Complexity:
Best Case: O(n log n), Occurs when the pivot element divides the array into two equal halves.
Average Case O(n log n), On average, the pivot divides the array into two parts, but not necessarily equal.
Worst Case: O(n²), Occurs when the smallest or largest element is always chosen as the pivot (e.g., sorted arrays).
Space Complexity:
O(log n) for the recursive stack space in the best and average cases, O(n) in the worst case due to the depth of recursion.
Auxiliary Space: O(n)


Why Choose Quick Sort?
Fastest on average (O(n log n)) → Works efficiently on large datasets.
In-place sorting (O(log n) space) → No extra memory like Merge Sort.
Efficient for general-purpose sorting → Used in libraries like Python's sorted() (Timsort uses Quick Sort internally).
Best when pivot is chosen wisely → Avoids worst-case O(n²) behavior.

When Not to Use Quick Sort
If you need stability → Quick Sort is not stable (relative order of equal elements may change).
If worst-case O(n²) is a concern → Merge Sort guarantees O(n log n) always.
For nearly sorted arrays → Insertion Sort is better (O(n)).

'''


def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1 ## This is the index of the pivot after partitioning

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

my_array = [8, 4, 7, 1, 6, 2, 3, 5]
quicksort(my_array)
print("Sorted array:", my_array)


''' 
Python uses an algorithm called Timsort (a hybrid sorting algorithm) for sort() and sorted().

About Timsort:
It's a hybrid of Merge Sort and Insertion Sort.
It was designed to perform very well on real-world data.
It is stable (maintains relative order of equal elements).

Time Complexity:
Best: O(n) (on nearly sorted data)
Average/Worst: O(n log n)

🧠 Why not Quick Sort?
Quick Sort is not stable.
In the worst case, Quick Sort is O(n²), which is risky.
Timsort guarantees better performance and safety.
'''