class Solution:
    def isHappy(self, n: int) -> bool:
        def getnext(n):
            s=0
            while n:
                s +=(n%10)**2
                n //=10
            return s
        s,f=n,getnext(n)
        while f !=1 and s !=f:
            s=getnext(s)
            f=getnext(getnext(f))
        return f==1

'''SOLVED BY ADIT MUGDHA DAS'''