class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for i in range(2 ** len(nums)):
            t = '0' * (len(nums) - len('{0:b}'.format(i))) + '{0:b}'.format(i)
            t_l = list()
            for k in range(len(t)):
                if t[k] != '0':
                    t_l.append(nums[k])
            result.add(tuple(sorted(t_l)))
        result = [list(i) for i in result]
        return result

