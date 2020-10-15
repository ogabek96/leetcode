class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        return num == self.sumDivisors(num)
    def sumDivisors(self, n):
        sum = 0
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                if n / i == i:
                    sum+=i
                else:
                    sum+=i
                    sum+=n/i
        return sum - n