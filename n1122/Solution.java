package n1122;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.List;

public class Solution {
  public static void main(String[] args) {

    // testcases:
    System.out.println(Arrays.toString(relativeSortArray(new int[]{2,3,1,3,2,4,6,7,9,2,19}, new int[]{2,1,4,3,9,6})));
    System.out.println(Arrays.toString(relativeSortArray(new int[]{28,6,22,8,44,17}, new int[]{22,28,8,6})));
    System.out.println(Arrays.toString(relativeSortArray(new int[]{1,0}, new int[]{0})));
    System.out.println(Arrays.toString(relativeSortArray(new int[]{2,0,3,2}, new int[]{2})));
    System.out.println(Arrays.toString(relativeSortArray(new int[]{4,0,0,7,6,3,7,5}, new int[]{7})));
    System.out.println(Arrays.toString(relativeSortArray(new int[]{12,3,0,9,13,2,5,12,2,7,10,14,13,12,6,15}, new int[]{12})));
    System.out.println(Arrays.toString(relativeSortArray(new int[]{48,23,7,0,48,12,51,38,17,2,1,22,16,58,28,21,37,36,19,35,26,55,45,5,0,36,62,27,55,37,18,26,27,17,39,57,30,37,38,8,60,22,1,34,58,41,63,53,32,63,27,52,15,24,37,36,34,54,21,47,16,3,21,15}, new int[]{1,5,51,45})));
  }

  public static int[] relativeSortArray(int[] arr1, int[] arr2) {
    Map<Integer, Integer> countMap = new HashMap<>(); 

    // -> (element, number of occurrences). - tc: o(n)
    for (int num : arr1) {
      countMap.put(num, countMap.getOrDefault(num, 0) + 1);
    }

    int[] result = new int[arr1.length];
    int index = 0;

    
    // fill the "result" array and remove from the hash the value read. - tc:  o(m)
    for (int i : arr2) {
      int count = countMap.get(i);
      while (count > 0) {
        result[index++] = i;
        count--;
      }
      countMap.remove(i);
    }

    // sort the remaining elements adds them to the "result" array. - tc: o(klogk) *k = n - m
    List<Integer> remaining = new ArrayList<>(countMap.keySet());
    Collections.sort(remaining);
    for (int num : remaining) {
      int count = countMap.get(num);
      while (count > 0) {
        result[index++] = num;
        count--;
      }
    }

    return result;
  }

  /*
   * tc: o((n + m) + klogk)
   * sc: o(n)
   */
}
