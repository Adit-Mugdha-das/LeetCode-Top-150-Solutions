class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,col=len(board),len(board[0])
        path=set()
        def backtrack(r,c,i):
            if i==len(word):
                return True
            if i<0 or r<0 or r>=row or c<0 or c>=col or board[r][c]!=word[i] or (r,c) in path:
                return False
            path.add((r,c))
            res=backtrack(r+1,c,i+1) or backtrack(r,c+1,i+1) or backtrack(r-1,c,i+1) or backtrack(r,c-1,i+1)
            path.remove((r,c))
            return res
        for i in range(row):
            for j in range(col):
                if backtrack(i,j,0):
                    return True
        return False

'''SOLVED BY ADIT MUGDHA DAS'''