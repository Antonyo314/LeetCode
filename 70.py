class Solution:
    def fib(self, n):
        a = 1
        b = 1
        for i in range(n-1):
            b, a = a + b, b
        return b

    def climbStairs(self, n: int) -> int:
        return self.fib(n)

