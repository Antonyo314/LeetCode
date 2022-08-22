class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = list()
        for i in s:
            if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122 or 48 <= ord(i) <= 57:
                if 65 <= ord(i) <= 90:
                    res.append(chr(ord(i) + 32))
                else:
                    res.append(i)

        return res == res[::-1]