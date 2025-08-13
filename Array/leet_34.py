'''
34.Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value. If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

'''

def searchRange(self, nums, target):
        def find_first(nums,target):
            left=0
            right=len(nums) - 1
            first=-1
            while(left<=right):
                mid = (left+right)//2
                if(nums[mid]==target):
                    first=mid
                    right=mid-1
                elif(nums[mid]>target):
                    right=mid-1
                else:
                    left=mid+1
            return first

        def find_last(nums,target):
            left=0
            right=len(nums) - 1
            last=-1
            while(left<=right):
                mid = (left+right)//2
                if(nums[mid]==target):
                    last=mid
                    left=mid+1
                elif(nums[mid]>target):
                    right=mid-1
                else:
                    left=mid+1
            return last
            
        return(find_first(nums,target),find_last(nums,target))

