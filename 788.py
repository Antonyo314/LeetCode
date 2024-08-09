class Solution:
    def __init__(self):
        self.change = ['2', '5', '6', '9']
        self.bad = ['3', '4', '7']

    def rotatedDigits(self, n: int) -> int:
        res = 0
        for k in range(1, n + 1):

            for i in self.bad:
                if i in str(k):
                    break
            else:
                for i in self.change:
                    if i in str(k):
                        res += 1
                        break

        return res
