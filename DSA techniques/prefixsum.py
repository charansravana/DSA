
'''

The prefix sum technique is a powerful method used to quickly calculate the sum of elements in a sub-array of a given array. It helps reduce the time complexity of multiple range sum queries from O(n) to O(1) after some O(n) preprocessing.

'''
## Leetcode - 1480
def prefix_sum(arr):
    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]
    return arr

arr= [1, 2, 3, 4, 5]
prefix_sum_arr = prefix_sum(arr.copy())
print("Prefix Sum Array:", prefix_sum_arr)


'''
Leetcode - 560
Given an array of integers nums and an integer k, return the total number of sub-arrays whose sum equals to k. A sub-array is a contiguous non-empty sequence of elements within an array.

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

'''

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_counts = {0: 1}
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num

            if (prefix_sum - k) in prefix_counts:
                count += prefix_counts[prefix_sum - k]
                
            if prefix_sum in prefix_counts:
                prefix_counts[prefix_sum] += 1
            else:
                prefix_counts[prefix_sum] = 1

        return count

nums= [1, 1, 1]
k = 2
solution = Solution()
result = solution.subarraySum(nums, k)
print("Number of subarrays with sum equal to k:", result)