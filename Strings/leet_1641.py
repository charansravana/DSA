'''
1614. Maximum Nesting Depth of the Parentheses
Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.

Example 1:
Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation:
Digit 8 is inside of 3 nested parentheses in the string.

Example 2:
Input: s = "(1)+((2))+(((3)))"
Output: 3
Explanation:
Digit 3 is inside of 3 nested parentheses in the string.

Example 3:
Input: s = "()(())((()()))"
Output: 3

'''

def maxDepth(s):
    depth=0
    maxx=0
    for i in s:
        if i=='(':
            depth+=1
            maxx=max(maxx,depth)
        elif i==')':
            depth-=1
    return maxx

s="8*((1*(5+6))*(8/6))"
print(maxDepth(s))