class Solution:
    mem = [None] * 31
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1 or N == 2:
            return 1
        if self.mem[N] != None:
            return self.mem[N]
        else:
            self.mem[N] = self.fib(N - 1) + self.fib(N - 2)
            return self.mem[N]
