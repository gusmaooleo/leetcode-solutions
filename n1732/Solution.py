class Solution:
  def largestAltitude(self, gain: list[int]) -> int:
    gain = [0] + gain

    sum = 0
    for i in range(len(gain)):
      sum += gain[i]
      gain[i] = sum
    
    return max(gain)
        