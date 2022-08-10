class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = list()
        while len(matrix) > 0:
            n = len(matrix)
            m = len(matrix[0])

            if m <= 1 or n <= 1:
                for i in matrix:
                    res.extend(i)
                return res

            for i in range(m - 1):
                res.append(matrix[0][i])
            for i in range(n - 1):
                res.append(matrix[i][m - 1])
            for i in range(m - 1, 0, -1):
                res.append(matrix[n - 1][i])
            for i in range(n - 1, 0, -1):
                res.append(matrix[i][0])

            matrix = matrix[1:-1]
            matrix = [i[1:-1] for i in matrix]

        return res

