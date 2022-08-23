class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        arr = [i for i in range(1, n ** 2 + 1)]
        res = [[0] * n for i in range(n)]

        i_l, i_r = 0, n - 1
        j_l, j_r = 0, n - 1

        i, j = 0, 0
        k = 0
        while i_r - i_l >= 1:
            while i <= i_r:
                res[j][i] = arr[k]
                i += 1
                k += 1
            i_r -= 1
            i -= 1
            j += 1
            while j <= j_r:
                res[j][i] = arr[k]
                j += 1
                k += 1
            j_r -= 1
            j -= 1
            i -= 1
            while i >= i_l:
                res[j][i] = arr[k]
                i -= 1
                k += 1
            j_l += 1
            i += 1
            j -= 1
            while j >= j_l:
                res[j][i] = arr[k]
                j -= 1
                k += 1
            i_l += 1
            j += 1
            i += 1
        if i_l == i_r:
            res[j_l][i_l] = arr[-1]
        elif i_r - i_l == 1:
            res[j_l][i_l] = arr[-4]
            res[j_r][i_l] = arr[-1]
            res[j_l][i_r] = arr[-3]
            res[j_r][i_r] = arr[-2]
        return res