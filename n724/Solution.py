class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
      nums = [0] + nums
      s = 0
      for i in range(len(nums)):
        s += nums[i]
        nums[i] = s
        
      for i in range(1, len(nums)):
        if nums[-1] - nums[i] == nums[i - 1]:
          return i - 1
      
      return -1
        
      
      
i = Solution()

print(i.pivotIndex([2,1,-1]))