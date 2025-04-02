class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r,m=Counter(ransomNote),Counter(magazine)
        for c in r:
            if r[c]>m[c]:
                return False
        return True

'''SOLVED BY ADIT MUGDHA DAS'''