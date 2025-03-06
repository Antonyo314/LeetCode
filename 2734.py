class Solution:
    @staticmethod
    def shift_back_char(ch):
        if 'a' <= ch <= 'z':
            return chr((ord(ch) - ord('a') - 1) % 26 + ord('a'))
        return ch


    def smallestString(self, s: str) -> str:
        change = False
        res =''
        t = 0
        change_was = False
        for i in range(len(s)):

            if (i==len(s)-1 or s[i] !='a') and not change_was:
                change = True
                change_was = True
                t = i


            if change and i>t and s[i]=='a':
                res+=s[i:]
                return res


            if change:
                res+=self.shift_back_char(s[i])
            else:
                res+=s[i]
        return res

Solution().smallestString('cbabc')