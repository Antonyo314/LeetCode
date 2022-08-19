from functools import cache


class Solution:
    def __init__(self):
        self.possible_values = [str(i) for i in range(1, 27)]

    @cache
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 1

        else:
            if s[0] in self.possible_values and s[:2] in self.possible_values and len(s) >= 2:
                return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
            elif s[0] in self.possible_values:
                return self.numDecodings(s[1:])
            else:
                return 0

