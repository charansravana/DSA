'''
Two pointers are simply two variables that move (left to right, or toward each other) across a data structure like an array or string to solve a problem more efficiently than brute force.

Usually:
One pointer starts from the beginning.
Another starts from the end (or both start together).
You move them based on a condition (e.g., sum comparison, matching elements, etc.).

Two Pointers	   :  O(n) or O(n log n)	
Traditional Loops  :  O(n²)


Situation                           Reason for Two Pointers

Find pair sum in sorted array	    Minimize time by narrowing range
Check palindrome	                Compare start and end characters
Remove duplicates	                Write unique values at right place
Merge two arrays	                Maintain order efficiently
Longest substring without repeats	Expand and shrink substring window
Reverse array or linked list	    Swap ends moving inward
Move zeros / partition array	    Rearranging in-place
Detect cycle in linked list	        Fast and slow pointer meet


leetcode - 167,11

'''

## pseudo code for two pointers technique
def two_pointer_sum(arr, target):
    left = 0
    right = len(arr) - 1
    # Assuming arr is sorted
    if not arr or len(arr) < 2:
        return None
    while (left<right):
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return left,right
        elif current_sum < target:
            left +=1
        else:
            right -=1
    return None
print(two_pointer_sum([2,7,11,15],9))

# Leetcode-167 , for 1-based indexing 
def twoSum(numbers, target):
        left=0
        right=len(numbers)-1
        while(left<right):
            current_sum = numbers[left]+numbers[right]
            if current_sum == target:
                return left+1,right+1
            elif current_sum < target:
                left +=1
            else:
                right -=1
        return None
print(twoSum([2,7,11,15],9))


# # leetcode - 17
# def letterCombinations(digits):
#     if not digits:
#         return []
    
#     digit_to_char = {
#         '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
#         '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
#     }
    
#     def backtrack(index, path):
#         if index == len(digits):
#             combinations.append("".join(path))
#             return
        
#         possible_chars = digit_to_char[digits[index]]
#         for char in possible_chars:
#             path.append(char)
#             backtrack(index + 1, path)
#             path.pop()

#     combinations = []
#     backtrack(0, [])
#     return combinations
# print(letterCombinations("23"))


# Merging two sorted arrays using two pointers technique 
def merge_two_arrays(self,arr1,arr2):
    merged=[]
    i,j,k=0,0,0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]< arr2[j]:
            if not merged or merged[-1] != arr1[i]:  #for duplicate removal 
                merged.append(arr1[i])
            i=i+1
        elif arr1[i]>arr2[j]:
            if not merged or merged[-1]!= arr2[j]:  #for duplicate removal
                merged.append(arr2[j])
            j+=1
        else:
            if not merged or merged[-1] != arr1[i]:  #for duplicate removal
                merged.append(arr1[i])
            i += 1
            j += 1
    return merged + arr1[i:] + arr2[j:]

arr1=[1,2,9,11]
arr2=[1,2,4,6,7]
print(merge_two_arrays(None, arr1, arr2))  # Output: [1, 2, 3, 4, 5, 6]

