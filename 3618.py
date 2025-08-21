from typing import List


class Solution:
    def splitArray(self, nums: List[int]) -> int:
        primes = [-1] * max(len(nums), 2)
        primes[0] = primes[1] = False

        for i in range(2, len(primes)):
            if primes[i] == -1:
                primes[i] = True
            for j in range(2, len(primes) // i + 1):
                if i * j < len(primes):
                    primes[i * j] = False

        res = 0

        for i in range(len(nums)):
            if primes[i]:
                res += nums[i]
            else:
                res -= nums[i]

        return abs(res)
