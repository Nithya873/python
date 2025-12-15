class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        pr = 0
        pra = 0
        c = 0

        for i in range(len(prices) - 1):
            if prices[i] - prices[i + 1] != 1:
                n = (pra - pr) + 1
                x = n * (n + 1) // 2
                c += x
                pr = i + 1
                pra = i + 1
            else:
                pra += 1

        n = (pra - pr) + 1
        x = n * (n + 1) // 2
        c += x

        return c
