class Solution:
    @staticmethod
    def close(a):
        d_ = {'(': ')', '{': '}', '[': ']'}
        if a in d_:
            return d_[a]
        else:
            return 0

    def isValid(self, s: str) -> bool:
        while len(s) > 0:
            changed = False
            for i in range(len(s) - 1):
                if self.close(s[i]) == s[i + 1]:
                    s = s[:i] + s[i + 2:]
                    changed = True
                    break
            if not changed:
                return False
        return True

