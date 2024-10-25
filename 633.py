class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(0, int((c//2) ** 0.5 + 1)):
            k = (c - i ** 2) ** 0.5
            if int(k) == k:
                return True

        return False
