class Solution:
  def buildArray(self, nums: list[int]) -> list[int]:
    copy = nums.copy()
    for i in range(len(nums)):
      nums[i] = copy[copy[i]]
    
    return nums