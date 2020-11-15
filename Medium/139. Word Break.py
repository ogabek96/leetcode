class Solution:
    def wordBreak(self, s: str, wordDict: List[str]):
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for ind in range(1, len(s) + 1):
            for word in wordDict:
                if dp[ind - len(word)] and s[:ind].endswith(word):
                    dp[ind] = True
        return dp[len(s)]