class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=0
        for i in nums:
            n ^=i
        return n
    
'''SOLVED BY ADIT MUGDHA DAS'''