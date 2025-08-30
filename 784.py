class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = [s]
        for i, s_ in enumerate(s):
            if 65 <= ord(s_) <= 90:
                for t in res.copy():
                    t = t[:i] + chr(ord(t[i]) + 32) + t[i + 1:]
                    res.append(t)
            elif 97 <= ord(s_) <= 122:
                for t in res.copy():
                    t = t[:i] + chr(ord(t[i]) - 32) + t[i + 1:]
                    res.append(t)
        return res