class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        l=0
        maxx=0
        for r in range(len(s)):
            if s[r] in dic:
                l=max(l,dic[s[r]]+1)
            dic[s[r]]=r
            maxx=max(maxx,r-l+1)
        return maxx
    
    '''SOLVED BY ADIT MUGDHA DAS'''