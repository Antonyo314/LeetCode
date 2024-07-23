class Solution:
    def addDigits(self, num: int) -> int:
        if num % 9 == 0:
            if num == 0:
                return 0
            else:
                return 9
        else:
            return num % 9
