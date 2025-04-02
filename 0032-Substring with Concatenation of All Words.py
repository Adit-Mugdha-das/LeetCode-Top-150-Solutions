class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        wl,n,tl=len(words[0]),len(words),len(words)*len(words[0])
        wc,r=Counter(words),[]
        for i in range(wl):
            l,rp,c=i,i,Counter()
            while rp+wl<=len(s):
                t=s[rp:rp+wl]
                rp +=wl
                if t in wc:
                    c[t] +=1
                    while c[t]>wc[t]:
                        c[s[l:l+wl]] -=1
                        l +=wl
                    if rp-l==tl:
                        r.append(l)
                else:
                    c.clear()
                    l=rp
        return r
    
    '''SOLVED BY ADIT MUGDHA DAS'''