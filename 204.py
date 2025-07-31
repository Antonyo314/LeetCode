class Solution:
    def countPrimes(self, n: int) -> int:
        primes = {i: True for i in range(2, n)}
        res = 0
        for i in primes.keys():
            if primes[i]:
                res += 1
                j = 2
                while j * i < n:
                    primes[j * i] = False
                    j += 1
            else:
                continue

        return res

Solution().countPrimes(n=10)
