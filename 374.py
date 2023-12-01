class Solution:
    def guessNumber(self, n: int) -> int:
        a = 1
        b = n
        while b - a > 1:
            if guess((a + b) // 2) == 0:
                return (a + b) // 2
            elif guess((a + b) // 2) == -1:
                b = (a + b) // 2
            else:
                a = (a + b) // 2

        if guess(a) == 0:
            return a
        else:
            return b