class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        s,c,m=0,0,nums[0]
        for x in nums:
            c=max(x,c+x)
            m=max(m,c)
            s +=x
        c,n=0,nums[0]
        for x in nums:
            c=min(x,c+x)
            n=min(n,c)
        return max(m,s-n) if m>0 else m

'''SOLVED BY ADIT MUGDHA DAS'''