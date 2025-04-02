class Solution:
    def spiralOrder(self, m: List[List[int]]) -> List[int]:
        if not m:
            return []
        r,t,b,l,rt=[],0,len(m)-1,0,len(m[0])-1
        while t<=b and l<=rt:
            for c in range(l,rt+1):
                r.append(m[t][c])
            t +=1
            for rr in range(t,b+1):
                r.append(m[rr][rt])
            rt -=1
            if t<=b:
                for c in range(rt,l-1,-1):
                    r.append(m[b][c])
                b -=1
            if l<=rt:
                for rr in range(b,t-1,-1):
                    r.append(m[rr][l])
                l +=1
        return r
    
'''SOLVED BY ADIT MUGDHA DAS'''