class Solution:
    def isPalindrome(self, s: str) -> bool:
        f=''.join(c.lower() for c in s if c.isalnum())
        return f==f[::-1]
    
    '''SOLVED BY ADIT MUGDHA DAS'''