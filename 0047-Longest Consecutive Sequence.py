class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s,m=set(nums),0
        for x in s:
            if x-1 not in s:
                y=x
                while y in s:
                    y +=1
                m=max(m,y-x)
        return m

'''SOLVED BY ADIT MUGDHA DAS'''