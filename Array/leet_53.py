'''
53.Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The sub-array [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The sub-array [1] has the largest sum 1.

'''

def maxSubArray(self, nums):
        curSum = 0
        maxSum = nums[0]

        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSum = max(maxSum, curSum)
        
        return maxSum 