from typing import List


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        return sorted(score, key=lambda arr: arr[k], reverse=True)


Solution().sortTheStudents(score=[[3, 4], [5, 6]], k=0)
