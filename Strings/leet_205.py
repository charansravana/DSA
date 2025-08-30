'''
205. Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true
Explanation:
The strings s and t can be made identical by:
Mapping 'e' to 'a'.
Mapping 'g' to 'd'.

Example 2:
Input: s = "foo", t = "bar"
Output: false
Explanation:
The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:
Input: s = "paper", t = "title"
Output: true

'''

def isIsomorphic(s,t):
    map_s={}
    map_t={}

    for chS,chT in zip(s,t):

        if chS in map_s and map_s[chS] != chT:
            return False
        if chT in map_t and map_t[chT] != chS:
            return False
        
        map_s[chS] = chT
        map_t[chT] = chS

    return True

s="egg"
t="add"
print(" Two stings are isomorphic or not: ", isIsomorphic(s,t))


'''
zip() is used to combine two (or more) iterables (like lists, strings, tuples) element by element.
It creates pairs (or tuples) from each element at the same index.

Syntax:
zip(iterable1, iterable2, ...)

How it works:
Takes the first element from each iterable and makes a tuple.
Takes the second element from each iterable and makes another tuple.
Continues this until the shortest iterable ends.

Example 1: Two lists
a = [1, 2, 3]
b = ['x', 'y', 'z']
print(list(zip(a, b)))

Output:
[(1, 'x'), (2, 'y'), (3, 'z')]


Example 2: Different lengths
a = [1, 2, 3, 4]
b = ['a', 'b']
print(list(zip(a, b)))

Output:
[(1, 'a'), (2, 'b')]   [ Stops at the shortest iterable (b in this case) ]

Example 3: Strings
s = "egg"
t = "add"
print(list(zip(s, t)))

Output:
[('e', 'a'), ('g', 'd'), ('g', 'd')]

'''