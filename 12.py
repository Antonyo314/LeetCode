class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}

        res = ''
        for i in d.keys():
            t = num // i

            res += d[i] * t

            num %= i

        replace_d = {'VIIII': 'IX', 'IIII': 'IV', 'LXXXX': 'XC', 'XXXX': 'XL', 'DCCCC': 'CM', 'CCCC': 'CD'}
        for k, v in replace_d.items():
            res = res.replace(k, v)

        return res