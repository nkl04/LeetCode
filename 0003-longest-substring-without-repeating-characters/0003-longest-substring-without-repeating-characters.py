class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLen = 0
        seen = set()
        right,left = 0,0

        for right in range(n):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            maxLen = max(maxLen, right - left + 1)
        return maxLen

        