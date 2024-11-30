from typing import List

class Solution:
    @staticmethod
    def change(arr):
        while True:
            changed = False
            for i in range(len(arr) - 1, 0, -1):
                if arr[i] == '.' and arr[i - 1] == '#':
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
                    changed = True

            if not changed:
                return arr

    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        res = []

        for box in boxGrid:
            box = self.change(box)

            res.append(box)
        return list(map(list, zip(*res[::-1])))


Solution().rotateTheBox(boxGrid=[["#", "#", "*", ".", "*", "."],
                                 ["#", "#", "#", "*", ".", "."],
                                 ["#", "#", "#", ".", "#", "."]])
