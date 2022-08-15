class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = list()
        for i in range(2 ** len(nums)):
            t = '{0:b}'.format(i)
            t = '0' * (len(nums) - len(t)) + t
            l = list()

            for x in range(len(t)):
                if t[x] != '0':
                    l.append(nums[x])

            res.append(l)
        return res