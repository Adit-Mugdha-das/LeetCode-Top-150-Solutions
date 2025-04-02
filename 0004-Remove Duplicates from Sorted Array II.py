class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k=0
        for n in nums:
            if k<2 or n !=nums[k-2]:
                nums[k]=n
                k +=1
        return k
    '''SOLVED BY ADIT MUGDHA DAS'''