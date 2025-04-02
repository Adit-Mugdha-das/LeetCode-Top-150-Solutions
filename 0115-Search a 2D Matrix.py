class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m,n=len(matrix),len(matrix[0])
        l,r=0,m*n-1
        while l<=r:
            mid=(l+r)//2
            row,col=divmod(mid,n)
            midval=matrix[row][col]
            if midval==target:
                return True
            elif midval<target:
                l=mid+1
            else:
                r=mid-1 
        return False

'''SOLVED BY ADIT MUGDHA DAS'''