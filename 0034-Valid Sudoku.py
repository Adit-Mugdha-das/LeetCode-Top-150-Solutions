class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for i in range(9)]
        cols=[set() for i in range(9)]
        boxes=[set() for i in range(9)]
        for r in range(9):
            for c in range(9):
                n=board[r][c]
                if n==".":
                    continue
                bind=(r//3)*3+(c//3)
                if n in rows[r] or n in cols[c] or n in boxes[bind]:
                    return False
                rows[r].add(n)
                cols[c].add(n)
                boxes[bind].add(n)
        return True

'''SOLVED BY ADIT MUGDHA DAS'''