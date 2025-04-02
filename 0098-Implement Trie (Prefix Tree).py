class Trie:
    def __init__(self):
        self.t={}
        self.e="#"
    def insert(self, word: str) -> None:
        t=self.t
        for c in word:
            if c not in t:
                t[c]={}
            t=t[c]
        t[self.e]=True

    def search(self, word: str) -> bool:
        t=self.t
        for c in word:
            if c not in t:
                return False
            t=t[c]
        return self.e in t
    def startsWith(self, prefix: str) -> bool:
        t=self.t
        for c in prefix:
            if c not in t:
                return False
            t=t[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

'''SOLVED BY ADIT MUGDHA DAS'''