class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=0
        dic={}
        for i in range(len(nums)):
            if nums[i] in dic:
                if i-dic[nums[i]]<=k:
                    return True
            dic[nums[i]]=i
        return False


'''SOLVED BY ADIT MUGDHA DAS'''