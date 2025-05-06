class Solution:
  def gcdOfStrings(self, str1: str, str2: str) -> str: 
    greatest = str1 if len(str1) > len(str2) else str2
    lowest = str2 if len(str1) > len(str2) else str1
      
    while len(lowest) > 0:
      befGreatest = greatest
      greatest = greatest.removeprefix(lowest)
      
      if len(greatest) == len(befGreatest):
        return ""
      
      if len(greatest) < len(lowest):
        prevGreatest = greatest
        greatest = lowest
        lowest = prevGreatest
        
       
    return greatest
      
      
i = Solution()

print(i.gcdOfStrings("ABCABC", "ABC"))             # "ABC"
print(i.gcdOfStrings("ABABAB", "ABAB"))            # "AB"
print(i.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))            # "TAUXX"
print(i.gcdOfStrings("ABC", "ABCABCABC"))          # "ABC"
print(i.gcdOfStrings("XYZ", "XYZXYZXYZXYZ"))       # "XYZ"
print(i.gcdOfStrings("A", "A"))                    # "A"

print(i.gcdOfStrings("ABCABC", "DEFDEF"))          # ""
print(i.gcdOfStrings("LEET", "CODE"))              # ""

print(i.gcdOfStrings("ABCAB", "ABC"))              # ""
print(i.gcdOfStrings("ABCABCX", "ABC"))            # ""

print(i.gcdOfStrings("ABABABAB", "ABAB"))          # "ABAB"

print(i.gcdOfStrings("A" * 1000, "A" * 250))        # "A * 250"

print(i.gcdOfStrings("AABAABAAB", "AAB"))          # "AAB"

print(i.gcdOfStrings("ABCABCABC", "ABCABC"))       # "ABC"
print(i.gcdOfStrings("ABAB", "AB"))                # "AB"
print(i.gcdOfStrings("ABAB", "BA"))                # ""

print(i.gcdOfStrings("A", "AA"))                   # "A"
print(i.gcdOfStrings("AB", "ABAB"))                # "AB"
print(i.gcdOfStrings("B", "BBBBBBB"))              # "B"
print(i.gcdOfStrings("BB", "BBB"))                 # "B"

print(i.gcdOfStrings("ABABABAC", "AB"))            # ""

