class Solution:
    def merge(self, iv: List[List[int]]) -> List[List[int]]:
        iv.sort()
        r=[iv[0]]
        for s,e in iv[1:]:
            if s <=r[-1][1]:
                r[-1][1]=max(r[-1][1],e)
            else:
                r.append([s,e])
        return r

'''SOLVED BY ADIT MUGDHA DAS'''