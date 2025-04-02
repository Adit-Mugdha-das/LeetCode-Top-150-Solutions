class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        tcount=Counter(t)  
        wcount={} 
        req=len(tcount) 
        formed=0  
        l=0  
        minlen=float("inf")
        minwin= ""
        for r in range(len(s)):
            c=s[r]
            wcount[c]=wcount.get(c,0)+1
            if c in tcount and wcount[c]==tcount[c]:
                formed +=1
            while formed==req:
                if r-l+1<minlen:
                    minlen=r-l+1
                    minwin=s[l:r+1]
                lchar=s[l]
                wcount[lchar] -=1
                if lchar in tcount and wcount[lchar]<tcount[lchar]:
                    formed -=1
                l +=1  
        return minwin
    
    '''SOLVED BY ADIT MUGDHA DAS'''