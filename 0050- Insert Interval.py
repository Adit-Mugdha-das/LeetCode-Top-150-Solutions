class Solution:
    def insert(self, iv: List[List[int]], ni: List[int]) -> List[List[int]]:
        r,i=[],0
        while i<len(iv) and iv[i][1]<ni[0]:
            r.append(iv[i])
            i +=1
        while i<len(iv) and iv[i][0]<=ni[1]:
            ni[0]=min(ni[0],iv[i][0])
            ni[1]=max(ni[1],iv[i][1])
            i +=1
        r.append(ni)
        return r+iv[i:]

'''SOLVED BY ADIT MUGDHA DAS'''