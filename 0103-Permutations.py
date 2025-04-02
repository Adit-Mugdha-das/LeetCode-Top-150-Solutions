class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        num=itertools.permutations(nums)
        return [list(p) for p in num]
    
    '''SOLVED BY ADIT MUGDHA DAS'''