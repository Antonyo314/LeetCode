class Solution(object):
    def singleNumber(self, nums):
        s = set()
        for i in nums:
            if i in s:
                s.remove(i)
            else:
                s.add(i)

        return list(s)[0]
