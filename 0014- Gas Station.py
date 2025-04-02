class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totaltank=0
        curtank=0
        st=0
        for i in range(len(gas)):
            totaltank +=gas[i]-cost[i]
            curtank +=gas[i]-cost[i]
            if curtank<0:
                st=i+1
                curtank=0
        return st if totaltank >= 0 else -1
    
    '''SOLVED BY ADIT MUGDHA DAS'''