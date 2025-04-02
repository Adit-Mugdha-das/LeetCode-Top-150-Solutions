class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s

        rows=['']*numRows
        currow=0
        goingdown=False
        for c in s:
            rows[currow] +=c
            if currow==0 or currow==numRows-1:
                goingdown = not goingdown
            currow +=1 if goingdown else -1
        return ''.join(rows)
    
    
    '''SOLVED BY ADIT MUGDHA DAS'''