'''
128. Longest Consecutive Sequence (Medium)

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

'''

def longestConsecutive(self,nums):
    num_set=set(nums)
    longest_sub=1

    for num in num_set:
        if num-1 in num_set:
            continue
        else:
            current_num=num
            current_sub=1

            while current_num+1 in num_set:
                current_num += 1
                current_sub += 1

            longest_sub = max(longest_sub , current_sub )
    return longest_sub

#example usage
nums = [100, 4, 200, 1, 3, 2, 5, 99, 98, 101, 102, 97]
solution = longestConsecutive(None, nums)
print(f"The length of the longest consecutive sequence is: {solution}")
