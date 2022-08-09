class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        strs_ = [''.join(sorted(s)) for s in strs]

        d = dict()
        for ind, i in enumerate(strs_):
            if i not in d:
                d[i] = []
            d[i].append(ind)

        res = list()
        for v in d.values():
            res.append([strs[i] for i in v])

        return res