import math
class Solution:
    def trailingZeroes(self, n: int) -> int:
        c=0
        while n>=5:
            n//=5
            c+=n
        return c

'''SOLVED BY ADIT MUGDHA DAS'''