from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        visited = []
        visited_ = set()
        d = {}

        for pair in adjacentPairs:
            if pair[0] not in d.keys():
                d[pair[0]] = []
            d[pair[0]].append(pair[1])
            if pair[1] not in d.keys():
                d[pair[1]] = []
            d[pair[1]].append(pair[0])

        start = [k for k in d.keys() if len(d[k]) == 1][0]
        visited.append(start)
        visited_.add(start)
        while len(visited) < len(adjacentPairs) + 1:
            if d[start][0] not in visited_:
                start = d[start][0]
                visited.append(start)
                visited_.add(start)
            else:
                start = d[start][1]
                visited.append(start)
                visited_.add(start)

        return visited


Solution().restoreArray(adjacentPairs=[[2, 1], [3, 4], [3, 2]])
