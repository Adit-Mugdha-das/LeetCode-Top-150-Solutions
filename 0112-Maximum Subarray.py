class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_end=0
        max_sofar=float('-inf')
        for r in range(len(nums)):
            max_end+=nums[r]
            if max_end<nums[r]:
                max_end=nums[r]
            if max_end>max_sofar:
                max_sofar=max_end
        return max_sofar
    
'''SOLVED BY ADIT MUGDHA DAS'''