class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof=0
        l=0
        for r in range(1,len(prices)):
            tmp=prices[r]-prices[l]
            if tmp>=0:
                prof+=tmp
            l+=1
        return prof

        '''SOLVED BY ADIT MUGDHA DAS'''