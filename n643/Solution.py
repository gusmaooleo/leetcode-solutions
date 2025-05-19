class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        fs = sum(nums[:k])
        greatest = fs
        for i in range(len(nums) - k):
            fs = fs - nums[i] + nums[i + k]
            greatest = max(greatest, fs)
        return greatest / k
      
i = Solution()

print(i.findMaxAverage([4, -1, 2, -7, 5, -3, 6], 4))