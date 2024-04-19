class Solution:
    def minFlips(self, target: str) -> int:
        while len(target) > 0 and target[0] == '0':
            target = target[1:]

        t = []
        k = -1
        for i in target:
            if i != k:
                t.append(i)
                k = i
        return len(t)
