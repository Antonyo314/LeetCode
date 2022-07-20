from functools import reduce

class Solution:
    d = {2: ['a', 'b', 'c'],
         3: ['d', 'e', 'f'],
         4: ['g', 'h', 'i'],
         5: ['j', 'k', 'l'],
         6: ['m', 'n', 'o'],
         7: ['p', 'q', 'r', 's'],
         8: ['t', 'u', 'v'],
         9: ['w', 'x', 'y', 'z']
         }

    @staticmethod
    def f(l1, l2):
        res_lists = []
        for i in range(len(l1)):
            for j in range(len(l2)):
                res_lists.append(l1[i] + l2[j])

        return res_lists

    def letterCombinations(self, digits: str) -> List[str]:

        lists = [self.d[int(i)] for i in digits]

        if len(lists) == 0:
            return []

        res = reduce(lambda x, y: self.f(x, y), lists)

        return res

