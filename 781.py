from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d = {}

        for answer in answers:
            if answer not in d:
                d[answer] = 0
            d[answer] += 1

        for answer in answers:
            a = d[answer]
            b = answer + 1
            d[answer] = a // b * b + (a % b > 0) * b
        return sum(d.values())
