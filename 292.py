class Solution:
    def canWinNim(self, n: int) -> bool:
        n %= 4
        if 1 <= n <= 3:
            return True
        else:
            return False
