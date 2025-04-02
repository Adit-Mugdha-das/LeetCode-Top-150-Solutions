class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram=defaultdict(list)
        for i in strs:
            sword=''.join(sorted(i))
            anagram[sword].append(i)
        return list(anagram.values())
            
        
'''SOLVED BY ADIT MUGDHA DAS'''