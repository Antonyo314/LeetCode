class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        res = 0
        piles = sorted(piles)
        n = len(piles) // 3
        piles = piles[n:]
        for i in range(0, len(piles), 2):
            res += piles[i]
        return res

