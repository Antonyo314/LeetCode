class Solution:
    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        for i in range(2, int(n ** 0.5 + 1)):
            if n % i == 0:
                return False
        return True

    @cache
    def f(self, n):
        if n not in self.d_is_prime:
            return 0
        if self.d_is_prime[n]:
            return 0
        for p in self.primes:
            if p > n:
                return 0
            if n % p == 0:
                if n // p in self.primes and n != p ** 2:
                    return 1 + n + p + n // p
                elif round(n ** (1 / 3), 5) in self.primes:
                    return 1 + round(n ** (1 / 3)) + round(n ** (2 / 3)) + n

                else:
                    return 0
        return 0

    def sumFourDivisors(self, nums: List[int]) -> int:

        self.d_is_prime = {}

        for i in range(10 ** 5 + 1):
            if self.is_prime(i):
                self.d_is_prime[i] = True
            for j in range(2, 10 ** 5):
                if i * j > 10 ** 5:
                    break
                self.d_is_prime[i * j] = False

        self.primes = [i for i in self.d_is_prime.keys() if self.d_is_prime[i] == True]

        return sum([self.f(num) for num in nums])
