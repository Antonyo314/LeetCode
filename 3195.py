from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        min_i = 10_000
        min_j = 10_000

        max_i = 0
        max_j = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    min_i = min(min_i, i)
                    min_j = min(min_j, j)
                    max_i = max(max_i, i)
                    max_j = max(max_j, j)

        return (max_i - min_i + 1) * (max_j - min_j + 1)



Solution().minimumArea([[0,1,0],[1,0,1]])

