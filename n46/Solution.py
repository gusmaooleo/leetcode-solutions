
class Solution:
  def permute(self, nums: list[int], r: list = None, s: list = None) -> list[list[int]]:
    if r is None and s is None:
      r = []
      s = []

    if len(s) == len(nums):
      r.append(s.copy())
      return

    for i in nums:
      if i not in s:
        s.append(i)
        self.permute(nums, r, s)
        s.pop()

    return r


n = Solution()

print(n.permute([1, 2, 3]))
print(n.permute([1, 2, 3, 4]))
print(n.permute([1]))

# subset problem soved with backtracking algorithm ->
'''
  Teminology ->
  Backtracking: is an algorithmic technique where the goal is to get all solutions to a problem using the brute force approach.
'''

# time complexity: o(n * n!) - better explanation at ./permutations_tree.png
# space complexity: o(n * n!) ->
'''
  For each element on the res (r) list we have n elements, but the final answer is related to the total permutations for n entry (n!).
  So the final space complexity is o(n times n!).
'''

# how it should work:
# -> (1)
# [(1), 2, 3]
# [1, (2), 3]
# [1, 2, (3)]

# [(1), 2, 3]
# [1, 2, (3)]
# [1, (2), 3]

# -> (2)
# [1, (2), 3]
# [(1), 2, 3]
# [1, 2, (3)]

# [1, (2), 3]
# [1, 2, (3)]
# [(1), 2, 3]

# -> (3)
# [1, 2, (3)]
# [(1), 2, 3]
# [1, (2), 3]

# [1, 2, (3)]
# [1, (2), 3]
# [(1), 2, 3]