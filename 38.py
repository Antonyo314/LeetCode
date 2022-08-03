class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n-1):
            l1, l2 = list(), list()
            t = '$'
            c = '$'
            for i in range(len(s)):
                if s[i] != t:
                    t = s[i]
                    l1.append(t)
                    if c != '$':
                        l2.append(c)
                    c = 1
                else:
                    c += 1
            l2.append(c)

            s = ''
            for a, b in zip(l1, l2):
                s += str(b) + a

        return s

