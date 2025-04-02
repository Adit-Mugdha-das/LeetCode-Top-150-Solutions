from functools import lru_cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        @lru_cache(None)
        def dp(i:int,j:int) -> bool:
            if i==len(s1) and j==len(s2):
                return True
            if i<len(s1) and s1[i]==s3[i+j] and dp(i+1,j):
                return True
            if j<len(s2) and s2[j]==s3[i+j] and dp(i,j+1):
                return True
            return False
        return dp(0,0)

'''SOLVED BY ADIT MUGDHA DAS'''