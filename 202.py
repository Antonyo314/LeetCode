class Solution:
    def happy(self, n, l):
        if n in l:
            return False

        l.add(n)

        if n == 1:
            return True

        s = str(n)
        res = 0
        for i in s:
            res += int(i) ** 2
        return self.happy(res, l)

    def isHappy(self, n: int) -> bool:
        return self.happy(n, set())