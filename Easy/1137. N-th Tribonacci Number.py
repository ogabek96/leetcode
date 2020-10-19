class Solution:
    mem = [None] * 38
    def tribonacci(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 0 or N == 1 or N == 2:
            return 1
        if self.mem[N] != None:
            return self.mem[N]
        else:
            self.mem[N] = self.tribonacci(N - 1) + self.tribonacci(N - 2) + self.tribonacci(N - 3)
            return self.mem[N]
