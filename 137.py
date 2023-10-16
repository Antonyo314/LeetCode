class Solution(object):
    def singleNumber(self, nums):
        d = {}
        for n in nums:
            if n in d:
                if d[n] == 2:
                    del d[n]
                else:
                    d[n] = 2
            else:
                d[n] = 1

        return list(d.keys())[0]