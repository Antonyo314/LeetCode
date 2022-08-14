class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []

        for i in matrix:
            arr.extend(i)

        a = 0
        b = len(arr) - 1

        while b - a > 1:
            t = a + (b - a) // 2
            if arr[t] == target:
                return True
            if arr[t] > target:
                b = t
            else:
                a = t

        if target != arr[a] and target != arr[b]:
            return False
        else:
            return True