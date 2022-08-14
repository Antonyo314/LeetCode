class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        list_range = list(range(1, n + 1))
        res = list()
        max_ = len('{0:b}'.format(2 ** n - 1))
        for i in range(2 ** n):
            t = '{0:b}'.format(i)
            t = '0' * (max_ - len(t)) + t
            t = [i for i in t]
            t_ = [i for i in t if i != '0']

            if len(t_) == k:
                l = list()

                for i in range(len(t)):
                    if t[int(i)] == '1':
                        l.append(list_range[int(i)])
                res.append(l)
        return res