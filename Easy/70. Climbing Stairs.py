class Solution:
    mem = [None] * 46
    def climbStairs(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
        if N == 2:
            return 2
        if self.mem[N] != None:
            return self.mem[N]
        else:
            self.mem[N] = self.climbStairs(N - 1) + self.climbStairs(N - 2)
            return self.mem[N]
