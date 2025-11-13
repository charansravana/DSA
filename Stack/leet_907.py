'''
907. Sum of Subarray Minimums [Medium]
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

Example 1:
Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.

Example 2:
Input: arr = [11,81,94,43,3]
Output: 444
'''

def sumSubarrayMins(arr):    
    MOD = 10**9 + 7
    n = len(arr)
    
    stack = []
    prev_smaller = [0]*n
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        prev_smaller[i] = i - stack[-1] if stack else i + 1
        stack.append(i)
    
    stack = []
    next_smaller = [0]*n
    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        next_smaller[i] = stack[-1] - i if stack else n - i
        stack.append(i)
    
    result = 0
    for i in range(n):
        result += arr[i] * prev_smaller[i] * next_smaller[i]
    
    return result % MOD

arr = [3,1,2,4]
print(sumSubarrayMins(arr))  # Output: 17