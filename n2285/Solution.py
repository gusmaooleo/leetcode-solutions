

def maximumImportance(n: int, roads: list[list[int]]) -> int:
  d = {}

  for i in range(n):
    d[i] = 0
  
  for j in roads:
    d[j[0]] += 1
    d[j[1]] += 1

   
  print(d)



# print(maximumImportance(5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]))
print(maximumImportance(5, [[0,1],[0,2],[1,2],[1,3],[2,3],[2,4]]))