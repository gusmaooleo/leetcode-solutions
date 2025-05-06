class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
      flowerbed = [0] + flowerbed + [0]
      size = len(flowerbed)

      for i in range(1, size - 1):
          if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
            flowerbed[i] = 1
            n -= 1
            if n == 0:
              return True

      return n <= 0


i = Solution()

# print(i.canPlaceFlowers([1,0,0,0,0,1], 1))      # True
# print(i.canPlaceFlowers([1,0,0,0,1], 2))        # False
# print(i.canPlaceFlowers([1,0,0,0,1,0], 2))      # False
# print(i.canPlaceFlowers([1,0,0,0,1], 1))        # True
# print(i.canPlaceFlowers([0,1,0], 1))            # False
# print(i.canPlaceFlowers([0], 1))                # True
# print(i.canPlaceFlowers([1], 0))                # True
# print(i.canPlaceFlowers([0,0,0,0,0], 2))        # True
# print(i.canPlaceFlowers([1,0,0,0,0,1], 1))      # True
# print(i.canPlaceFlowers([1,0,1,0,1], 1))        # False
# print(i.canPlaceFlowers([0,0,1,0,0], 2))        # True
# print(i.canPlaceFlowers([0,0,1,0,0], 3))        # False
# print(i.canPlaceFlowers([0,0,0,0,1], 2))        # True
# print(i.canPlaceFlowers([1,0,0,0,0], 2))        # True
# print(i.canPlaceFlowers([1,0,0,0,0,0,1], 2))    # True
# print(i.canPlaceFlowers([0,0,0,0,0,0,0], 3))    # True


print(i.canPlaceFlowers([0, 0, 1], 1))  # True
print(i.canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2))  # True
print(i.canPlaceFlowers([0, 0, 0, 0, 1], 2))  # True


print(i.canPlaceFlowers([0, 0, 0, 0, 1], 2))  # True
print(i.canPlaceFlowers([0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1,
      0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0], 17))  # ✅ deveria ser False
