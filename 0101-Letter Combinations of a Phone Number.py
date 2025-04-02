class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letters={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        res=[]
        def backtrack(i,path):
            if len(path)==len(digits):
                res.append(path)
                return
            for j in digit_to_letters[digits[i]]:
                backtrack(i+1,path+j)
        if digits:
            backtrack(0,"")
        return res

'''SOLVED BY ADIT MUGDHA DAS'''