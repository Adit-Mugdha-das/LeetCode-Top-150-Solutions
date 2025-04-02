class Solution:
    def findMedianSortedArrays(self, n1: List[int], n2: List[int]) -> float:
        if len(n1)>len(n2):
            n1,n2=n2,n1
        m,n=len(n1),len(n2)
        l,r=0,m
        while l<=r:
            p1=(l+r)//2
            p2=(m+n+1)//2-p1
            l1=float('-inf') if p1==0 else n1[p1-1]
            r1=float('inf') if p1==m else n1[p1]
            l2=float('-inf') if p2==0 else n2[p2-1]
            r2=float('inf') if p2==n else n2[p2]
            if l1<=r2 and l2<=r1:
                if (m+n)%2==0:
                    return (max(l1,l2)+min(r1,r2))/2
                return max(l1,l2)
            elif l1>r2:
                r=p1-1
            else:
                l=p1+1

'''SOLVED BY ADIT MUGDHA DAS'''