class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        minheap=[]
        result=[]
        for i in range(min(len(nums1), k)):
            heappush(minheap,(nums1[i]+nums2[0],i,0)) 
        while k>0 and minheap:
            total,i,j=heappop(minheap)
            result.append([nums1[i],nums2[j]])
            k -=1
            if j+1<len(nums2):
                heappush(minheap,(nums1[i]+nums2[j+1],i,j+1))
        return result

'''SOLVED BY ADIT MUGDHA DAS'''