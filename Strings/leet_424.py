def characterReplacement(self, s, k):
    count = [0] * 26
    left = 0
    ans = 0
    max_count = 0

    for right in range(len(s)):
        index = ord(s[right]) - ord("A")
        count[index] += 1
        max_count = max(max_count, count[index])

        while (right - left + 1) - max_count > k:
            count[ord(s[left]) - ord("A")] -= 1
            left += 1

        ans = max(ans, right - left + 1)

    return ans
