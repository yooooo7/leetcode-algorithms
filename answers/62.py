class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        
        # m 是列数 n 是行数
        dp = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            dp[i][-1] = 1
        for j in range(m):
            dp[-1][j] = 1
        
        for row in range(n-2, -1, -1):
            for column in range(m-2, -1, -1):
                dp[row][column] = dp[row+1][column] + dp[row][column+1]
        
        return dp[0][0]