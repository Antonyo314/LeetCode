class Solution:
    def minimumSteps(self, s: str) -> int:
        d = {}
        zeros = len([i for i in s if i == '0'])
        res = 0
        for i in range(len(s)):
            if s[i] == '0':
                zeros -= 1
            else:
                res += zeros
            d[i] = zeros
        return res


Solution().minimumSteps('11110000')
