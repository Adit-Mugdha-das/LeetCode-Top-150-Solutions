class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph={i:[] for i in range(numCourses)}
        indeg={i:0 for i in range(numCourses)}
        for course,pre in prerequisites:
            graph[pre].append(course)
            indeg[course] +=1
        q=deque([course for course in indeg if indeg[course]==0])
        c=0
        while q:
            course=q.popleft()
            c+=1
            for n in graph[course]:
                indeg[n]-=1
                if indeg[n]==0:
                    q.append(n)
        return c==numCourses

'''SOLVED BY ADIT MUGDHA DAS'''