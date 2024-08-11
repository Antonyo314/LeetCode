from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        all_sizes = set(groupSizes)
        res = []
        for size in all_sizes:
            # print(size)
            temp = []
            for ind, i in enumerate(groupSizes):
                # print(ind, i)
                if i == size:
                    if len(temp) == 0:
                        temp = [[ind]]
                    elif len(temp[-1]) < i:
                        temp[-1].append(ind)
                    else:
                        temp.append([ind])
            res.extend(temp)
        return res


Solution().groupThePeople([3, 3, 3, 3, 3, 1, 3])
