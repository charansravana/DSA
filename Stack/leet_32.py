'''
32. Longest Valid Parentheses [Hard]
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0

'''

def longestValidParentheses(s):
    count=0
    stack=[-1]
    for i,ch in enumerate(s):
        if ch=='(':
            stack.append(i)
        else:
            stack.pop()
            
            if not stack:
                stack.append(i)
            else:
                count=max(count,i-stack[-1])
            
    return count
    
s="()(()"
print(longestValidParentheses(s))