class Solution:
    @staticmethod
    def is_palindrom(s):
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        max_ = -1
        max_s = ''
        for a, b in zip(range(len(s)), range(len(s))[1:]):
            i, j = a, b
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if j - i > max_:
                    max_ = j - i
                    max_s = s[i:j + 1]
                i -= 1
                j += 1

        for a, b in zip(range(len(s)), range(len(s))):
            i, j = a, b
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if j - i > max_:
                    max_ = j - i
                    max_s = s[i:j + 1]

                i -= 1
                j += 1

        return max_s