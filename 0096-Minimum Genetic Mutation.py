class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        bank=set(bank)
        q=deque([(startGene,0)])
        pchar=['A','C','G','T']
        while q:
            gene,mu= q.popleft()
            if gene==endGene:
                return mu
            for i in range(len(gene)):
                for c in pchar:
                    if c !=gene[i]:
                        mugene=gene[:i]+c+gene[i+1:]
                        if mugene in bank:
                            q.append((mugene,mu+1))
                            bank.remove(mugene)

        return -1

'''SOLVED BY ADIT MUGDHA DAS'''