class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i_s, j_s = list(), list()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    i_s.append(i)
                    j_s.append(j)

        for i in i_s:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        for j in j_s:
            for i in range(len(matrix)):
                matrix[i][j] = 0