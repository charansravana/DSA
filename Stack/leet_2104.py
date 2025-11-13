'''
2104. Sum of Sub Array Ranges [Medium]

You are given an integer array nums. The range of a Sub Array of nums is the difference between the largest and smallest element in the Sub Array.

Return the sum of all Sub Array ranges of nums.

A Sub Array is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,2,3]
Output: 4
Explanation: The 6 Sub Arrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.

Example 2:
Input: nums = [1,3,3]
Output: 4
Explanation: The 6 Sub Arrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[3], range = 3 - 3 = 0
[3], range = 3 - 3 = 0
[1,3], range = 3 - 1 = 2
[3,3], range = 3 - 3 = 0
[1,3,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.

Example 3:
Input: nums = [4,-2,-3,4,1]
Output: 59
Explanation: The sum of all Sub Array ranges of nums is 59.

'''

def subArrayRanges(nums):
    n = len(nums)
    
    # Helper function to calculate the sum of subarray minimums
    def sumOfSubarrayMins():
        stack = []
        left = [0] * n
        right = [0] * n
        
        for i in range(n):
            count = 1
            while stack and stack[-1][0] > nums[i]:
                count += stack.pop()[1]
            left[i] = count
            stack.append((nums[i], count))
        
        stack.clear()
        
        for i in range(n-1, -1, -1):
            count = 1
            while stack and stack[-1][0] >= nums[i]:
                count += stack.pop()[1]
            right[i] = count
            stack.append((nums[i], count))
        
        total = 0
        for i in range(n):
            total += nums[i] * left[i] * right[i]
        
        return total
    
    # Helper function to calculate the sum of subarray maximums
    def sumOfSubarrayMaxs():
        stack = []
        left = [0] * n
        right = [0] * n
        
        for i in range(n):
            count = 1
            while stack and stack[-1][0] < nums[i]:
                count += stack.pop()[1]
            left[i] = count
            stack.append((nums[i], count))
        
        stack.clear()
        
        for i in range(n-1, -1, -1):
            count = 1
            while stack and stack[-1][0] <= nums[i]:
                count += stack.pop()[1]
            right[i] = count
            stack.append((nums[i], count))
        
        total = 0
        for i in range(n):
            total += nums[i] * left[i] * right[i]
        
        return total
    
    return sumOfSubarrayMaxs() - sumOfSubarrayMins()

# Example usage:
nums1 = [1, 2, 3]
print(subArrayRanges(nums1))  # Output: 4

nums2 = [1, 3, 3]
print(subArrayRanges(nums2))  # Output: 4

nums3 = [4, -2, -3, 4, 1]
print(subArrayRanges(nums3))  # Output: 59