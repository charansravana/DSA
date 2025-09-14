"""
4.Longest Substring Without Repeating Characters (Medium)

Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

"""


def lengthOfLongestSubstring(self, s):
    if not s:
        return 0
    if len(s) == 1:
        return 1
    left = 0
    right = 0
    ans = 0
    seen = set()

    while right < len(s):
        c = s[right]
        while c in seen:
            seen.remove(s[left])
            left += 1
        seen.add(c)
        ans = max(ans, right - left + 1)
        right += 1
    return ans
