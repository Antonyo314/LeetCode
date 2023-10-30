class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10 ** 9 + 7

        if n == 1:
            return 5

        prev_a, prev_e, prev_i, prev_o, prev_u = 1, 1, 1, 1, 1

        for i in range(n-1):
            next_a = (prev_e + prev_i + prev_u) % mod
            next_e = (prev_a + prev_i) % mod
            next_i = (prev_e + prev_o) % mod
            next_o = prev_i % mod
            next_u = (prev_i + prev_o) % mod

            prev_a, prev_e, prev_i, prev_o, prev_u = next_a, next_e, next_i, next_o, next_u

        return (next_a + next_e + next_i + next_o + next_u) % mod