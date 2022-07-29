class Solution:
    def generate(self, l, a, b):
        if a == 0 and b == 0:
            return l
        elif a == 0:
            res = list()
            for i in l:
                res.extend(self.generate([i + ')'], a, b - 1))
            return res
        elif b > a:
            res = list()
            for i in l:
                res.extend(self.generate([i + ')'], a, b - 1))
                res.extend(self.generate([i + '('], a - 1, b))
            return res
        else:
            res = list()
            for i in l:
                res.extend(self.generate([i + '('], a - 1, b))
            return res

    def generateParenthesis(self, n: int) -> List[str]:
        a, b = n, n
        return self.generate([''], a, b)