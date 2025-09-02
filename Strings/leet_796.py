'''
796. Rotate String
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.
For example, if s = "abcde", then it will be "bcdea" after one shift.

Example 1:
Input: s = "abcde", goal = "cdeab"
Output: true

Example 2:
Input: s = "abcde", goal = "abced"
Output: false

'''

def rotateString(s,goal):
    for i in range(len(s)):
        t=s[i+1:]+s[:i+1]
        if t==goal:
            return True
    return False

s="abcde"
goal="bcdea"
print("Does the strings are rotation of each other: " , rotateString(s,goal))