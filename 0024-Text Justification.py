class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res=[]
        line,llen=[],0
        for word in words:
            if llen+len(word)+len(line)>maxWidth:
                for i in range(maxWidth-llen):
                    line[i%(len(line)-1 or 1)] +=' '
                res.append(''.join(line))
                line,llen=[],0
            line.append(word)
            llen +=len(word)
        res.append(' '.join(line).ljust(maxWidth))
        return res
        
        '''SOLVED BY ADIT MUGDHA DAS'''