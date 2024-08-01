from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        d = {}

        for a in arr:
            if a not in d:
                d[a] = 0
            d[a] += 1

        a = d.values()
        a = sorted(a, reverse=True)

        len_ = len(arr)
        len_ = len_ // 2 + len_ % 2

        t = 0
        for i in range(len(a)):
            print(f'i: {i}')
            t += a[i]
            if t >= len_:
                break

        return i + 1


Solution().minSetSize([3, 3, 3, 5, 5, 5])
