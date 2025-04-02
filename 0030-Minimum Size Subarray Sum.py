class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        n=len(nums)
        minsum=float('inf')
        total=0
        for r in range(n):
            total+=nums[r]
            while total>=target and l<n:
                minsum=min(minsum,r-l+1)
                total-=nums[l]
                l+=1
        return minsum if minsum!=float('inf') else 0
    
    '''SOLVED BY ADIT MUGDHA DAS'''