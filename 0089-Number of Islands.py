class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows,cols=len(grid),len(grid[0])
        ic=0
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        def bfs(r,c):
            q=deque([(r,c)])
            grid[r][c]='0'
            while q:
                row,col=q.popleft()
                for dr,dc in directions:
                    newr,newc=row+dr,col+dc
                    if 0<=newr<rows and 0<=newc<cols and grid[newr][newc]=='1':
                        grid[newr][newc]='0'
                        q.append((newr,newc))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1':
                    ic+=1
                    bfs(r,c)
        return ic

'''SOLVED BY ADIT MUGDHA DAS'''