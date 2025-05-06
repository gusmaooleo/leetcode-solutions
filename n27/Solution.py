class Solution:
  def removeElement(self, nums: list[int], val: int) -> int:
    lastNonValIndex = 0

    n = 0
    for i in range(len(nums)):
      if nums[i] != val:
        n += 1
        nums[lastNonValIndex] = nums[i]
        lastNonValIndex += 1

    for i in range(lastNonValIndex, len(nums)):
      nums[i] = None
    
    return n

a = [0,1,2,2,3,0,4,2]
i = Solution()

print(i.removeElement(a, 2))