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

leetcode problems: 643 , 3, 76 
'''

# Leetcode - 643. Maximum Average Sub-array I
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