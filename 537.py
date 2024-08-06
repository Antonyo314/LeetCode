class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a = int(num1.split('+')[0])
        b = int(num1.split('+')[1].split('i')[0])

        c = int(num2.split('+')[0])
        d = int(num2.split('+')[1].split('i')[0])

        a_res = a * c - b * d
        b_res = a * d + b * c

        return f'{a_res}+{b_res}i'
