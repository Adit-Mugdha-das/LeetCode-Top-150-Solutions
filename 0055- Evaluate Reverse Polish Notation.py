class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for t in tokens:
            if t in {"+","-","*","/"}:
                b=st.pop()
                a=st.pop()
                if t=="+":
                    st.append(a+b)
                elif t=="-":
                    st.append(a-b)
                elif t=="*":
                    st.append(a*b)
                elif t=="/":
                    st.append(int(a/b))
            else:
                st.append(int(t))
        return st[0]

'''SOLVED BY ADIT MUGDHA DAS'''