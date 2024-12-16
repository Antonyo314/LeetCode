from typing import List


class Solution:

    @staticmethod
    def patter_s(pattern):
        it = 0
        s = set()
        d = {}

        for char in pattern:
            if char not in s:
                s.add(char)
                d[char] = it
                it += 1

        pattern_str = ''

        for char in pattern:
            pattern_str += '_' + str(d[char])

        return pattern_str

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        pattern_str = self.patter_s(pattern)

        res = []

        for word in words:
            if self.patter_s(word) == pattern_str:
                res.append(word)

        return res


Solution().findAndReplacePattern(words=["abcdefghijkba"], pattern="qwertyuiopwqa")
