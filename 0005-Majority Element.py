class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        c=None
        for i in nums:
            if count==0:
                c=i
            count +=(1 if i==c else -1)
        return c

'''SOLVED BY ADIT MUGDHA DAS'''