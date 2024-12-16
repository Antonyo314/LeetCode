from typing import List


class Solution:
    @staticmethod
    def count(arr):
        k = len(arr) // 2
        a = arr[:k]
        b = arr[-k:]

        b = b[::-1]

        t = 0
        for i in range(len(a)):
            t += (a[i] + b[i]) % 2
        return t

    def minFlips(self, grid: List[List[int]]) -> int:
        rows = [row for row in grid]
        columns = [list(col) for col in list(zip(*grid))]
        rows_s = sum([self.count(row) for row in rows])
        columns_s = sum([self.count(column) for column in columns])

        return min(rows_s, columns_s)


Solution().minFlips(grid=[[0, 1], [0, 1], [0, 0]])

arr = [1, 2, 3]

k = len(arr) // 2
a = arr[:k]
b = arr[-k:]
print(a)
print(b)
