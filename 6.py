class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ''
        if numRows == 1:
            return s
        for k in range(numRows):
            j = 0

            while j * (numRows - 1) - k < len(s):
                if j * (numRows - 1) - k >= 0:
                    res += s[j * (numRows - 1) - k]
                if k != 0 and k != numRows - 1:
                    if j * (numRows - 1) + k < len(s):
                        res += s[j * (numRows - 1) + k]

                j += 2

        return res