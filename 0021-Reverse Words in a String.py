class Solution:
    def reverseWords(self, s: str) -> str:
        w=s.split()
        rw=w[::-1]
        return " ".join(rw)
    
    '''SOLVED BY ADIT MUGDHA DAS'''