class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            it = -1
            while abs(it) <= len(digits) and digits[it] == 9:
                it -= 1
            if abs(it) > len(digits):
                return [1] + [0] * len(digits)
            else:
                digits[it] += 1
                for i in range(it + 1, 0):
                    digits[i] = 0
                return digits