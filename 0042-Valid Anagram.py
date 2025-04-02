class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      vec1=[0]*26
      vec2=[0]*26
      m=len(s)
      n=len(t)
      if n!=m:
        return None
      for i in range(n):
        vec1[ord(s[i])-ord('a')] +=1
        vec2[ord(t[i])-ord('a')] +=1
      if(vec1==vec2):
        return True
     
      return False
  
'''SOLVED BY ADIT MUGDHA DAS'''