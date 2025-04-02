class Solution:
    def romanToInt(self, s: str) -> int:
        rtint = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total=0
        preval=0
        for c in reversed(s):
            curval=rtint[c]
            if curval<preval:
                total-=curval  
            else:
                total +=curval
            preval=curval
        return total

'''SOLVED BY ADIT MUGDHA DAS'''