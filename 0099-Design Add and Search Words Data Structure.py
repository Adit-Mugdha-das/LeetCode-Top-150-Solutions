class WordDictionary:
    def __init__(self):
        self.t={}
        self.e="#"
    def addWord(self, word: str) -> None:
        t=self.t
        for c in word:
            if c not in t:
                t[c]={}
            t=t[c]
        t[self.e]=True
    def search(self, word: str) -> bool:
        def dfs(t,i):
            if i==len(word):
                return self.e in t
            if word[i]=='.':
                return any(dfs(t[c],i+1) for c in t if c !=self.e)
            if word[i] not in t:
                return False
            return dfs(t[word[i]],i+1)
        return dfs(self.t,0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

'''SOLVED BY ADIT MUGDHA DAS'''