class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        v = {
          'a': True, 
          'e': True, 
          'i': True, 
          'o': True,
          'u': True, 
          'A': True, 
          'E': True, 
          'I': True, 
          'O': True, 
          'U': True
        }

        l = list(s)
        while i <= j and i != j:
          if v.get(l[i]) and v.get(l[j]):
            c = l[i]
            l[i] = l[j]
            l[j] = c
            i += 1
            j -= 1
            
          if not v.get(l[i]):
            i += 1
          if not v.get(l[j]):
            j -= 1
          
        return ''.join(l)
      
      
i = Solution()

print(i.reverseVowels("IceCreAm"))       # "AceCreIm"
print(i.reverseVowels("leetcode"))       # "leotcede"
print(i.reverseVowels("HELLO"))          # "HOLLE"
print(i.reverseVowels("aA"))             # "Aa"
print(i.reverseVowels("bcd"))            # "bcd" (sem vogais, não muda)
print(i.reverseVowels("UOIEAuoiea"))     # "aeiouAEIOU" (só vogais, todas invertidas)
print(i.reverseVowels("ProgrammingIsFun"))  # "PrigrammongIsFun" (vogais invertidas)
print(i.reverseVowels("rhythm"))         # "rhythm" (sem vogais)
print(i.reverseVowels("AEIOUaeiouAEIOU"))# "UOIEAuoieaUOIEA"
print(i.reverseVowels("SphinxOfBlackQuartzJudgeMyVow"))  # "SphunxOfBlackQeartzJidgemyVow"
print(i.reverseVowels(".a")) 

