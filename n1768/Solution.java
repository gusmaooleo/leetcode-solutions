package n1768;

public class Solution {

  public static void main(String[] args) {
    Solution a = new Solution();
    String ret = a.mergeAlternately("abcd", "pq");
    System.out.println(ret);
  }

  public String mergeAlternately(String word1, String word2) {
    int n1 = word1.length();
    int n2 = word2.length();
    StringBuilder ans = new StringBuilder(n1 + n2);

    int i = 0;
    while (i < n1 && i < n2) {
      ans.append(word1.charAt(i));
      ans.append(word2.charAt(i));
      i++;
    }

    ans.append(word1.substring(i));
    ans.append(word2.substring(i));

    return ans.toString();
  }
}
