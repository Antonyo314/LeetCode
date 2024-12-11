class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        N = len(rowSum)
        M = len(colSum)
        matrix = [[0 for _ in range(M)] for _ in range(N)]

        while True:
            upd = False
            for i in range(N):
                for j in range(M):
                    if rowSum[i] != 0 and colSum[j] != 0 and matrix[i][j] == 0:
                        t = min(rowSum[i], colSum[j])
                        rowSum[i] -= t
                        colSum[j] -= t
                        matrix[i][j] = t
                        upd = True

            if not upd:
                return matrix
