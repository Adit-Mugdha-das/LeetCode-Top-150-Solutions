class Solution:
    def simplifyPath(self, path: str) -> str:
        st=[]
        parts=path.split('/')
        for p in parts:
            if p=="..":
                if st:
                    st.pop()
            elif p and p != ".":
                st.append(p)
        return "/" + "/".join(st)

'''SOLVED BY ADIT MUGDHA DAS'''