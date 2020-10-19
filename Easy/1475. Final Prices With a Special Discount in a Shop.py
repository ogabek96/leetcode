class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        leng = len(prices)
        for i in range(leng):
            discount = 0
            j = i + 1
            while j > i and j < leng:
                if prices[j] <= prices[i]:
                    discount = prices[j]
                    break
                j+=1
            prices[i] -= discount
        return prices