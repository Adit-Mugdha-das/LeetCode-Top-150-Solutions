class Solution:
    def jump(self, nums: List[int]) -> int:
        res=0
        total,maxx=0,0
        if len(nums)==1:
            return 0
        for i in range(len(nums)):
            total=max(total,i+nums[i])
            if i==maxx:
                res+=1
                maxx=total
            if maxx>=len(nums)-1:
                return res


'''SOLVED BY ADIT MUGDHA DAS'''