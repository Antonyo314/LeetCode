class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        while i <= len(haystack) - len(needle):
            if needle == haystack[i:i + len(needle)] and i + len(needle) <= len(haystack):
                return i
            i += 1
        return -1
