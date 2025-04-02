class Solution:
    def solve(self, board: List[List[str]]) -> None:
        numrow=len(board)
        numcol=len(board[0])
        boarders=list(product(range(numrow),[0,numcol-1]))+list(product([0,numrow-1],range(numcol)))
        deltas=[[1,0],[0,-1],[-1,0],[0,1]]
        for r,c in boarders:
            if board[r][c]=='O':
                q=[(r,c)]
                board[r][c]='E'
                while q:
                    cr,cc=q.pop()
                    for dr,dc in deltas:
                        nr,nc=cr+dr,cc+dc
                        if 0<=nr<numrow and 0<=nc<numcol and board[nr][nc]=='O':
                            board[nr][nc]='E'
                            q.append((nr,nc))        
        for r in range(numrow):
            for c in range(numcol):
                if board[r][c]=='O':
                    board[r][c]='X'
                elif board[r][c]=='E':
                    board[r][c]='O'

'''SOLVED BY ADIT MUGDHA DAS'''