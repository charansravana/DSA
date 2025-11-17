'''
The Sliding Window Technique is a powerful optimization strategy for problems involving sub-arrays or substrings—especially when you want to analyze all contiguous blocks of elements without repeating work.

When to Use Sliding Window:
When you're dealing with contiguous sub-arrays/substrings.
You want to compute sum, max, min, average, or frequency of items in a window.
The brute-force approach uses nested loops → O(n²).
Sliding window reduces time to O(n).

Examples:fixed-size window 
Maximum sum of subarray of size k
Minimum sum of subarray of size k
Average of each subarray of size k
Why Sliding Window?
Recomputing the sum every time is wasteful. Just subtract the first element of the previous window and add the new one.

Examples: variable-size window
Longest substring without repeating characters
Smallest subarray with sum ≥ target
Longest subarray with at most k distinct numbers
Longest substring with same characters after k replacements
Why Sliding Window?
Expand the window to include new elements, and shrink it from the left when a condition breaks.

Examples:counting or frequency based problems
Count of anagrams of a pattern in a string
Check if a string contains a permutation of another
Minimum window substring containing all characters of another string
Why Sliding Window?
Maintain frequency maps while sliding the window. Adjust the window when frequency conditions are met.

leet-code problems: 643 , 3, 76 
'''

#pseudo code for sliding window technique
def sliding_window(arr,w):
    current_sum=0
    for i in range(w):
        current_sum+=arr[i]
    max_sum=current_sum
    for j in range(w,len(arr)):
        current_sum=current_sum-arr[j-w]+arr[j]
        if current_sum>max_sum:
            max_sum=current_sum
    return max_sum
# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
w = 3
print(sliding_window(arr, w))  # Output: 27 (sum of [8, 9, 10])


# Leet-code - 643. Maximum Average Sub-array I
def findMaxAverage(nums, k):
    current=0
    for i in range(k):
        current = (current+nums[i])
    maxx=current
    for j in range(k,len(nums)):
        current=current- nums[j-k] + nums[j]
        if current>maxx:
            maxx=current
    return maxx/k


# Example usage
# nums = [1, 12, -5, -6, 50,3]
# k = 4
nums =[3,3,4,3,0]
k =3
print(findMaxAverage(nums, k))  

