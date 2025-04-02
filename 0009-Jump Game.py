class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)-1
        goal=nums[n]
        for i in range(n,-1,-1):
            if i+nums[i]>=goal:
                goal=i
        return True if goal==0 else False
    
    '''SOLVED BY ADIT MUGDHA DAS'''