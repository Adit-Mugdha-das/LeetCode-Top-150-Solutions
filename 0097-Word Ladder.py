class Solution:
    def ladderLength(self, bw: str, ew: str, wl: list) -> int:
        s=set(wl)
        if ew not in s:
            return 0
        q=deque([(bw, 1)])
        while q:
            w,d=q.popleft()
            if w==ew:
                return d
            for i in range(len(w)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    nw=w[:i]+c+w[i+1:]
                    if nw in s:
                        s.remove(nw)
                        q.append((nw,d+1))
        return 0

'''SOLVED BY ADIT MUGDHA DAS'''