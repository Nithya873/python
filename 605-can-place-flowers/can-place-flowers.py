class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        o = 0
        z = 0
        for i in range(l):
            if (flowerbed[i] == 0 and
                (i == 0 or flowerbed[i-1] == 0) and
                (i == l-1 or flowerbed[i+1] == 0)):
                flowerbed[i] = 1
                o += 1
        if o >= n:
            return True
        else:
            return False
      

            



        