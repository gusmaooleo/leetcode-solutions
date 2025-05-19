class Solution:
    # def reverseWords(self, s: str) -> str:
    #   revString = ""
    #   word = ""
    #   s = s + " "
      
    #   for i in range(len(s)):
    #     if s[i] == " " and len(word) > 0:
    #       revString = word + " " + revString
    #       word = ""
    #     elif s[i] != " ":
    #       word += s[i]
      
    #   return revString[:len(revString) - 1]
    def reverseWords(self, s: str) -> str:
        words = s.split()
        answer=""
        for i in range(len(words)):
            answer = words[i] + " " + answer
        return answer[:-1]
    
i = Solution()

print(i.reverseWords("  hello world  "))
print(i.reverseWords("a good   example"))
print(i.reverseWords("the sky is blue"))
