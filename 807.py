class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:

        res = 0
        for i in range(len(grid[0])):
            for j in range(len(grid[0])):
                t = max(min(max(grid[i][:j] + grid[i][j + 1:]), max([a[j] for a in grid[:i] + grid[i + 1:]])),
                        grid[i][j]) - grid[i][j]

                res += t
                grid[i][j] += t

        return res
