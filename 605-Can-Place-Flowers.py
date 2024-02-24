class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and n > 0:
                flowerbed[i] = 1
                n -= 1
                if i > 0 and flowerbed[i - 1] != 0:
                    flowerbed[i] = 0
                    n += 1
                elif i < len(flowerbed) - 1 and flowerbed[i + 1] != 0:
                    flowerbed[i] = 0
                    n += 1
        return n == 0