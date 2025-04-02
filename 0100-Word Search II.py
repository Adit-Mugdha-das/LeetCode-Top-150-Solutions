
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def buildTrie():
            root=TrieNode()
            for w in words:
                node=root
                for c in w:
                    if c not in node.children:
                        node.children[c]=TrieNode()
                    node=node.children[c]
                node.word=w
            return root
        
        def dfs(r,c,node):
            char=board[r][c]
            if char not in node.children:
                return
            nnode=node.children[char]
            if nnode.word:
                res.add(nnode.word)
                nnode.word=None  
            board[r][c]="#"
            for dr,dc in [(-1, 0),(1, 0),(0, -1),(0, 1)]:
                nr,nc=r+dr,c+dc
                if 0<=nr<len(board) and 0<=nc<len(board[0]) and board[nr][nc] !="#":
                    dfs(nr,nc,nnode)
            board[r][c]=char
        root=buildTrie()
        res=set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r,c,root)
        return list(res)

'''SOLVED BY ADIT MUGDHA DAS'''