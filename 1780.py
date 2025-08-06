class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n >= 3:
            if n % 3 == 0:
                n /= 3
            elif (n - 1) % 3 == 0:
                n -= 1
                n /= 3
            else:
                break
        if n > 1:
            return False
        else:
            return True


Solution().checkPowersOfThree(12)
