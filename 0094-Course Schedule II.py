class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph={i:[] for i in range(numCourses)}
        indeg={i:0 for i in range(numCourses)}
        for course,pre in prerequisites:
            graph[pre].append(course)
            indeg[course]+=1
        q=deque([course for course in indeg if indeg[course]==0])
        od=[]
        while q:
            course=q.popleft()
            od.append(course)
            for n in graph[course]:
                indeg[n]-=1
                if indeg[n]==0:
                    q.append(n)
        return od if len(od)==numCourses else []

'''SOLVED BY ADIT MUGDHA DAS'''