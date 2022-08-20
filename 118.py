class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(numRows - 1):
            t = [1]

            for j, k in zip(range(len(res[-1])), range(1, len(res[-1]))):
                t.append(sum(res[-1][j:k + 1]))
            t.append(1)
            res.append(t)

        return res