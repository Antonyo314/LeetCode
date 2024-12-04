class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 == 0:
            n /= 2
            return int(n ** 2)
        else:
            n //= 2
            return int(n * (n + 1))

