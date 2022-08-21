class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        res = list()

        maxs = list()

        max_ = -1
        for price in prices[::-1]:
            if price > max_:
                max_ = price
            maxs.append(max_)
        maxs = maxs[::-1]

        for i in range(len(prices) - 1):
            res.append([prices[i], maxs[i]])

        res = [i[1] - i[0] for i in res]
        return max(max(res), 0)