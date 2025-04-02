class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        a=1
        pe=points[0][1]
        for s,e in points[1:]:
            if s>pe:
                a +=1
                pe=e
        return a

'''SOLVED BY ADIT MUGDHA DAS'''