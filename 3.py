class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_ = 0

        i, j = 0, 0

        while len(set(s[i:j])) == len(s[i:j]) and j <= len(s):
            max_ = max(max_, j - i)
            j += 1

            while i < j and len(set(s[i:j])) != len(s[i:j]):
                i += 1

        return max_