function mergeAlternately(word1: string, word2: string): string {
  const result: string[] = [];
  let i = 0;
  
  while(true) {
    if(i >= word1.length || i >= word2.length) {
      return result.join('') + word1.substring(i) + word2.substring(i);
    }
    result.push(word1[i], word2[i]);
    i++;
  }
};


console.log(mergeAlternately("abcd", "pq"));