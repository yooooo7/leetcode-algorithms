class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        
        if n <= 1 or s == s[::-1]:
            return n
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
        
        for left in range(n-2, -1, -1):
            for right in range(left + 1, n):
                if s[left] == s[right]:
                    dp[left][right] = dp[left+1][right-1] + 2
                else:
                    dp[left][right] = max(dp[left+1][right], dp[left][right-1])
        
        return dp[0][-1]