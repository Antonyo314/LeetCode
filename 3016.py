class Solution:
    def minimumPushes(self, word: str) -> int:
        d = {}

        for s in set(list(word)):
            d[s] = word.count(s)

        d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

        t = 0
        l = 1
        d_ = {}

        for k in d.keys():
            d_[k] = l
            t += 1
            if t == 8:
                t = 0
                l += 1

        res = 0

        for k in d.keys():
            res += d[k] * d_[k]

        return res


Solution().minimumPushes(word="aabbccddeeffgghhiiiiii")
