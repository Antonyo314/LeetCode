class Solution(object):

    def counter(self, n):
        res = 0
        while n > 0:
            t = n % 2
            if t > 0:
                res += 1
            n -= t
            n /= 2
        return res

    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [self.counter(i) for i in range(n+1)]
