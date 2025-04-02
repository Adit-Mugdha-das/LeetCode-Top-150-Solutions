class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        minvalue=0
        for r in range(len(prices)):
            if prices[r]<prices[l]:
                l=r
            minvalue=max(minvalue,prices[r]-prices[l])
        return minvalue
    
    '''SOLVED BY ADIT MUGDHA DAS'''