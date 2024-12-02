class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        counter = 0
        i = 1
        while True:
            if n % i == 0:
                counter += 1
            if i == n and counter < k:
                return -1

            if counter == k:
                return i
            i += 1
