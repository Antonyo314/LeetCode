class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()

        max_l = max([len(i) for i in s])

        for i in range(len(s)):
            s[i] += ' ' * (max_l - len(s[i]))

        res = []

        for i in range(max_l):
            res.append(''.join([j[i] for j in s]).rstrip())
        return res