'''
154.Maximum Product Sub-array (Medium)

Given an integer array nums, find a sub-array that has the largest product, and return the product.The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a sub-array.

'''

def maxProduct(self,nums):
        if not nums:
            return 0

        max_pro = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            if num < 0:
                cur_max, cur_min = cur_min, cur_max 
            cur_max = max(num, cur_max * num)
            cur_min = min(num, cur_min * num)
            max_pro = max(max_pro,cur_max)

        return max_pro