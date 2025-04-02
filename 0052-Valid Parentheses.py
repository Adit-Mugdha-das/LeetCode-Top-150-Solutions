class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        bmap={')':'(', '}':'{', ']':'['}
        for c in s:
            if c in bmap:
                tele=st.pop() if st else '#'
                if bmap[c] !=tele:
                    return False
            else:
                st.append(c)
        return not st
    
'''SOLVED BY ADIT MUGDHA DAS'''