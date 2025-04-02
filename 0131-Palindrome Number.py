class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        rev=0
        n=x
        while n:
            m=n%10
            rev=rev*10+m
            n//=10
        return True if rev==x else False
    
'''SOLVED BY ADIT MUGDHA DAS'''