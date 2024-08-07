from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        j = 1
        res = []
        while True:
            if len(set(s[:j]).intersection(set(s[j:]))) == 0:
                res.append(j)
                s = s[j:]
                j = 0
            if len(s) == 0:
                break
            j += 1

        return res


print(Solution().partitionLabels("ababcbacadefegdehijhklij"))
