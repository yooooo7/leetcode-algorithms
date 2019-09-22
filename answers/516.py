class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n <= 1 or s == s[::-1]: return n
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        for l in range(n-1, -1, -1):
            dp[l][l] = 1
            for r in range(l+1, n):
                if s[l] == s[r]:
                    dp[l][r] = dp[l+1][r-1] + 2
                else:
                    dp[l][r] = max(dp[l+1][r], dp[l][r-1])
        
        return dp[0][n-1]