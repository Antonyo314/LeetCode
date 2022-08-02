class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            t = list()
            for j in range(9):
                t.append(board[i][j])
            t = [i for i in t if i != '.']
            if len(set(t)) != len(t):
                return False
        for i in range(9):
            t = list()
            for j in range(9):
                t.append(board[j][i])
            t = [i for i in t if i != '.']
            if len(set(t)) != len(t):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                t = list()
                for i_ in range(i, i + 3):
                    for j_ in range(j, j + 3):
                        t.append(board[i_][j_])
                t = [i for i in t if i != '.']
                if len(set(t)) != len(t):
                    return False
        return True

