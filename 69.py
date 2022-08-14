class Solution:
    def mySqrt(self, x: int) -> int:
        t = 1
        while t * t <= x:
            t += 1
        t -= 1
        return t

