from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        t = [0, 0, 0]

        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                t[0] = max(triplet[0], t[0])
                t[1] = max(triplet[1], t[1])
                t[2] = max(triplet[2], t[2])

        return t == target
