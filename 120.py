class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        res = list()
        for i in range(len(triangle)):
            res.append(triangle[i])

        res[-1] = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(res[i])):
                res[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])

        return res[0][0]