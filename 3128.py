

class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        rows = {}
        for i in range(len(grid)):
            rows[i] = sum(grid[i])
        cols = {}
        for i in range(len(grid[0])):
            cols[i] = sum([g[i] for g in grid[:]])

        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    res += (grid[i][j]) * (rows[i] - 1) * (cols[j] - 1)

        return res

