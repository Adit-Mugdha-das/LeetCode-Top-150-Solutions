class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dp={}
        for i,n in enumerate(nums):
            c=target-n
            if c in dp:
                return [dp[c],i]
            dp[n]=i    
        return []

'''SOLVED BY ADIT MUGDHA DAS'''