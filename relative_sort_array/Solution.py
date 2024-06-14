from collections import Counter

def relativeSortArray(arr1: list[int], arr2: list[int]) -> list[int]:
  
  # -> (element, number of occurrences) as a dict. - tc: o(n)
  count = Counter(arr1)
  res = []

  # fill the res list with the corresponding number of occurrences for each value. - tc: o(m)
  for i in arr2:
    if i in count:
      res.extend([i] * count[i])
      del count[i]
          
  # sort the remaining values (merge?). - tc: o(klogk) *k = n - m
  remaining = sorted(count.elements())
  res.extend(remaining)
  
  return res

'''
  tc: o((n + m) + klogk)
  sc: o(n)
'''


# testcases:
# print(relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))
# print(relativeSortArray([28,6,22,8,44,17], [22,28,8,6]))
# print(relativeSortArray([1,0], [0]))
# print(relativeSortArray([2,0,3,2], [2]))
# print(relativeSortArray([4,0,0,7,6,3,7,5], [7]))
# print(relativeSortArray([12,3,0,9,13,2,5,12,2,7,10,14,13,12,6,15], [12]))
# print(relativeSortArray([48,23,7,0,48,12,51,38,17,2,1,22,16,58,28,21,37,36,19,35,26,55,45,5,0,36,62,27,55,37,18,26,27,17,39,57,30,37,38,8,60,22,1,34,58,41,63,53,32,63,27,52,15,24,37,36,34,54,21,47,16,3,21,15], [1,5,51,45]))