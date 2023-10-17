class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i = 0
        while True:
            if 4 ** i == n:
                return True
            if 4 ** i > n:
                return False
            i += 1
