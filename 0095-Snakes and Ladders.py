class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n=len(board)
        def getpos(square):
            r,c=divmod(square-1,n)
            row=n-1-r
            col=c if r%2==0 else n-1-c
            return row,col
        q=deque([(1,0)])
        vis=set()
        while q:
            sq,moves=q.popleft()
            if sq==n*n:
                return moves
            for nsq in range(sq+1,min(sq+6,n*n)+1):
                r,c=getpos(nsq)
                des=board[r][c] if board[r][c]!=-1 else nsq
                if des not in vis:
                    vis.add(des)
                    q.append((des,moves+1))
        
        return -1

'''SOLVED BY ADIT MUGDHA DAS'''