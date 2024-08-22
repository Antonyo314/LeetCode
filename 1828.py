from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        final_res = []
        for circle in queries:
            res = 0
            for point in points:
                x, y = point[0], point[1]
                x1, y1, r = circle
                if (x - x1) ** 2 + (y - y1) ** 2 <= r ** 2:
                    res += 1
            final_res.append(res)

        return final_res


Solution().countPoints(points=[[1, 3], [3, 3], [5, 3], [2, 2]], queries=[[2, 3, 1], [4, 3, 1], [1, 1, 2]])
