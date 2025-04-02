class Solution:
    def totalNQueens(self, n: int) -> int:
        col=set()
        posdig=set()
        negdig=set()
        board=[[0]*n for _ in range(n)]
        res=0
        def backtrack(r):
            nonlocal res
            if r==n:
                res+=1
                return
            for c in range(n):
                if c in col or (r+c) in posdig or (r-c) in negdig:
                    continue
                col.add(c)
                posdig.add((r+c))
                negdig.add((r-c))
                board[r][c]=1
                backtrack(r+1)
                col.remove(c)
                posdig.remove((r+c))
                negdig.remove((r-c))
                board[r][c]=0
        backtrack(0)
        return res 
    
    '''SOLVED BY ADIT MUGDHA DAS'''