from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        l = sum(wall[0])
        for arr in wall:
            t = 0
            for i in range(len(arr)):
                arr[i] += t
                t = arr[i]

        d = {}
        for arr in wall:
            for a in arr:
                if a not in d:
                    d[a] = 0
                d[a] += 1

        del d[l]

        return len(wall) - max(list(d.values()) + [0])


Solution().leastBricks(wall=[[1], [1], [1]])
