class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]

        for i in range(rowIndex):
            t = [1]

            for j, k in zip(range(len(res[-1])), range(1, len(res[-1]))):
                t.append(sum(res[-1][j:k + 1]))
            t.append(1)
            res.append(t)

        return res[-1]