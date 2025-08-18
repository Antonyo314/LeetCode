from typing import List


class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        possible = [-1 if p == 0 else p for p in possible]
        t = 0
        x = []
        for p in possible:
            t += p
            x.append(t)


        t = 0
        y = []
        for p in possible[::-1]:
            t += p
            y.append(t)

        for i in range(len(x) - 1):
            if x[i] > y[-i - 2]:
                return i + 1
        return -1


Solution().minimumLevels(possible=[0, 0])
