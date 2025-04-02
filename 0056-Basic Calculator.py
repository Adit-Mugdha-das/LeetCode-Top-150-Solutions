class Solution:
    def calculate(self, s: str) -> int:
        st,n,sign=[],0,1
        res=0
        for c in s:
            if c.isdigit():
                n=n*10+int(c)
            elif c in ['+','-']:
                res +=sign*n
                n=0
                sign=1 if c=='+' else -1
            elif c=='(':
                st.append(res)
                st.append(sign)
                res,sign=0,1
            elif c==')':
                res +=sign*n
                res *=st.pop()
                res +=st.pop()
                n=0
        return res+sign*n
    
    '''SOLVED BY ADIT MUGDHA DAS'''