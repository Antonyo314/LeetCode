class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0

        secret_ = ''
        guess_ = ''
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secret_ += secret[i]
                guess_ += guess[i]

        cows = 0
        for i in set(secret_):
            cows += min(guess_.count(i), secret_.count(i))

        return f'{bulls}A{cows}B'