class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def back(i,path):
            if len(path)==k:
                res.append(path.copy())
                return
            for j in range(i,n+1):
                path.append(j)
                back(j+1,path)
                path.pop()
        back(1,[])
        return res
        
'''SOLVED BY ADIT MUGDHA DAS'''