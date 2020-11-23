class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0]*len(s) for i in range(len(s))]
        cnt = 0
        for i in range(len(s)):
            dp[i][i] = 1
            cnt+=1
        for col in range(1, len(s)):
            for row in range(col):
                if row == col - 1 and s[col] == s[row]:
                    dp[row][col] = 1
                    cnt+=1
                elif dp[row + 1][col - 1] == 1 and s[col] == s[row]:
                    cnt+=1
                    dp[row][col] = 1
        return cnt