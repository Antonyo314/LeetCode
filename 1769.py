from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes_inds = []

        for i, boxe in enumerate(boxes):
            if boxe == '1':
                boxes_inds.append(i)

        res = []

        for i in range(len(boxes)):
            s = 0
            for boxe_ind in boxes_inds:
                s += abs(boxe_ind - i)
            res.append(s)
        return res


Solution().minOperations(boxes="001011")
