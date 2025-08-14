from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = [int(timePoint[:2]) * 60 + int(timePoint[3:]) for timePoint in timePoints]
        print(timePoints)
        timePoints = [24 * 60 if timePoint == 0 else timePoint for timePoint in timePoints]
        timePoints = sorted(timePoints)

        temp = [b - a for a, b in zip(timePoints, timePoints[1:])]

        return min(min(temp), timePoints[0] + 24 * 60 - timePoints[-1])


Solution().findMinDifference(timePoints=["23:59", "00:00"])
