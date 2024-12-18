class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows_d = {}
        for arr in grid:
            t = '_'.join([str(a) for a in arr])
            if t not in rows_d:
                rows_d[t] = 0
            rows_d[t] += 1

        cols = []
        for i in range(len(grid[0])):
            col = [g[i] for g in grid]
            cols.append(col)

        cols_d = {}
        for arr in cols:
            t = '_'.join([str(a) for a in arr])
            if t not in cols_d:
                cols_d[t] = 0
            cols_d[t] += 1

        intersection = set(rows_d).intersection(cols_d)

        res = 0
        for k in intersection:
            res += rows_d[k] * cols_d[k]

        return res
