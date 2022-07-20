class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        d_ = {'IX': 'VIIII', 'IV': 'IIII', 'XC': 'LXXXX', 'XL': 'XXXX', 'CM': 'DCCCC', 'CD': 'CCCC'}

        for k, v in d_.items():
            s = s.replace(k, v)

        res = 0

        for i in s:
            res += d[i]

        return res


