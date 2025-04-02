class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        w=s.split()
        if len(pattern) !=len(w):
            return False
        m1,m2={},{}
        for c, word in zip(pattern,w):
            if (c in m1 and m1[c] !=word) or (word in m2 and m2[word] !=c):
                return False
            m1[c],m2[word]=word,c
        return True

'''SOLVED BY ADIT MUGDHA DAS'''