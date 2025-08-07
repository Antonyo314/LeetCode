from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer0 = list(set([match[0] for match in matches]).difference([match[1] for match in matches]))
        d = {}

        for match in matches:
            if match[1] not in d:
                d[match[1]] = 0
            d[match[1]] += 1


        answer1 = [k for k in d.keys() if d[k] == 1]
        return [sorted(answer0), sorted(answer1)]

Solution().findWinners(matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]])