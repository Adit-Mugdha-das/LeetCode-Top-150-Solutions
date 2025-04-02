class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r,c=len(m),len(m[0])
        fr=any(m[0][j]==0 for j in range(c))
        fc=any(m[i][0]==0 for i in range(r))
        for i in range(1,r):
            for j in range(1,c):
                if m[i][j]==0:
                    m[i][0]=m[0][j]=0
        for i in range(1,r):
            if m[i][0]==0:
                for j in range(1,c):
                    m[i][j]=0

        for j in range(1,c):
            if m[0][j]==0:
                for i in range(1,r):
                    m[i][j]=0
        if fr:
            for j in range(c):
                m[0][j]=0
        if fc:
            for i in range(r):
                m[i][0]=0

        
'''SOLVED BY ADIT MUGDHA DAS'''