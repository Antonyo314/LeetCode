from functools import cache



class Solution:

    def __init__(self):
        self.rules_dict = {'a': ['e'], 'e': ['a', 'i'], 'i': ['a', 'e', 'o', 'u'], 'o': ['i', 'u'], 'u': ['a']}
        self.characters = ['a', 'e', 'i', 'o', 'u']
        self.mod = 10 ** 9 + 7

    @cache
    def countPermutation(self, n, prev_ch):

        if n == 0:
            return 1

        result = 0

        if prev_ch == '':
            for ch in self.characters:
                result += self.countPermutation(n - 1, ch)
                result %= self.mod
        else:
            for ch in self.rules_dict[prev_ch]:
                result += self.countPermutation(n - 1, ch)
                result %= self.mod

        return result

    def countVowelPermutation(self, n: int) -> int:
        return self.countPermutation(n, '')