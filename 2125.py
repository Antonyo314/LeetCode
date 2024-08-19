class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        arr = []
        for i in bank:
            t = sum([int(j) for j in i])
            if t != 0:
                arr.append(t)

        if len(arr) <= 1:
            return 0

        else:
            res = 0
            for i, j in zip(arr, arr[1:]):
                res += i * j
        return res
