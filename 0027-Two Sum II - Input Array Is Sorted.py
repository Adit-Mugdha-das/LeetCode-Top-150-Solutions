class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        while l<r:
            cursum=numbers[l]+numbers[r]
            if cursum==target:
                return [l+1,r+1]
            elif cursum<target:
                l +=1
            else:
                r -=1
                
    '''SOLVED BY ADIT MUGDHA DAS'''