from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        for a, b in zip(prices, prices[1:]):
            if b > a:
                res += b - a
        return res
