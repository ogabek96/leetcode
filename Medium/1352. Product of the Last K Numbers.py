class ProductOfNumbers:
  
    def __init__(self):
        self.prods = []
    def add(self, num: int) -> None:
        if num == 0:
            self.prods = []
        elif len(self.prods) == 0:
            self.prods = [num]
        else:
            self.prods.append(self.prods[-1] * num)
    def getProduct(self, k: int) -> int:
        if k > len(self.prods):
            return 0
        ind = len(self.prods) - 1 - k
        if ind < 0:
            return self.prods[-1]
        return self.prods[-1] // self.prods[ind]
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)