class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph=defaultdict(list)
        for i,(u,v) in enumerate(equations):
            graph[u].append((v,values[i]))
            graph[v].append((u,1/values[i]))
        def helper(start,end):
            if start not in graph or end not in graph:
                return -1
            visited=set()
            q=[([1.0,start])]
            while q:
                cur_dis,cur_node=heapq.heappop(q)
                if cur_node==end:
                    return cur_dis
                if start==end:
                    return 1.0
                visited.add(cur_node)
                for v,w in graph[cur_node]:
                    if v not in visited:
                        heapq.heappush(q,(w*cur_dis,v))
            return -1
        res=[]
        for u,v in queries:
            res.append(helper(u,v))
        return res
    
'''SOLVED BY ADIT MUGDHA DAS'''