class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pro=sorted(zip(capital,profits))
        maxheap=[]  
        i=0
        n=len(profits)
        for _ in range(k):
            while i<n and pro[i][0]<=w:
                heappush(maxheap,-pro[i][1])  
                i +=1
            if not maxheap:
                break
            w +=-heappop(maxheap)  
        return w

'''SOLVED BY ADIT MUGDHA DAS'''