class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(1, n + 1):
            for j in range(1, i):
                a = (i - j) * j
                b = dp[i - j] * j
                c = dp[i]
                dp[i] = max(a, b, c)
        return dp[n]