from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        positive = [i for i in nums if i >= 0]
        negative = set([i for i in nums if i < 0])

        for i in range(len(positive)):
            for j in range(i + 1, len(positive)):
                if -(positive[i] + positive[j]) in negative:
                    res.append(tuple(sorted([positive[i], positive[j], -(positive[i] + positive[j])])))

        positive = set([i for i in nums if i >= 0])
        negative = [i for i in nums if i < 0]

        for i in range(len(negative)):
            for j in range(i + 1, len(negative)):
                if -(negative[i] + negative[j]) in positive:
                    res.append(tuple(sorted([negative[i], negative[j], -(negative[i] + negative[j])])))

        return list([list(i) for i in set(res)])


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
