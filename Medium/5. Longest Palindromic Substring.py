class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [len(s) * [0] for i in range(len(s))]
        a = 0
        b = 0
        for i in range(len(s)):
            dp[i][i] = 1
        for col in range(1, len(s)):
            for row in range(col):
                if row == col - 1 and s[row] == s[col]:
                    dp[row][col] = 1
                    if col - row > b - a:
                        a = row
                        b = col
                elif dp[row + 1][col - 1] == 1 and s[row] == s[col]:
                    if col - row > b - a:
                        a = row
                        b = col
                    dp[row][col] = 1
        return s[a:b + 1]