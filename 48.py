class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = list(zip(*matrix))

        for i in range(len(m)):
            m[i] = m[i][::-1]

        m = [list(i) for i in m]
        matrix[:] = m