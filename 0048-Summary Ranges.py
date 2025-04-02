class Solution:
    def summaryRanges(self, n: List[int]) -> List[str]:
        if not n:
             return []
        r,s=[],n[0]
        for i in range(1,len(n)+1):
            if i==len(n) or n[i] !=n[i-1]+1:
                r.append(str(s) if s == n[i-1] else f"{s}->{n[i-1]}")
                if i<len(n): s=n[i]
        return r

'''SOLVED BY ADIT MUGDHA DAS'''