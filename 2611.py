from typing import List


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        diffs = [r1 - r2 for r1, r2 in zip(reward1, reward2)]
        ind = [index for index, _ in sorted(enumerate(diffs), key=lambda x: x[1])]
        if k > 0:
            ind1 = ind[-k:]
        else:
            ind1 = []
        ind2 = set(range(len(reward1))) - set(ind1)
        res = 0
        for i in ind1:
            res += reward1[i]
        for i in ind2:
            res += reward2[i]
        return res


Solution().miceAndCheese(reward1=[4], reward2=[5], k=0)
