class Solution:
    def minPathSum(self, grid: list) -> int:
        M, N = len(grid), len(grid[0])
        
        dp = [[0 for _ in range(N)] for _ in range(M)]
        
        dp[-1][-1] = grid[-1][-1]
        for j in range(N-2, -1, -1):
            val = grid[-1][j]
            dp[-1][j] = val + dp[-1][j+1]
        for i in range(M-2, -1, -1):
            val = grid[i][-1]
            dp[i][-1] = val + dp[i+1][-1]
        
        if M == 1 or N == 1:
            return dp[0][0]
        
        for row in range(M-2, -1, -1):
            for column in range(N-2, -1, -1):
                val = grid[row][column]
                dp[row][column] = val + min(dp[row+1][column], dp[row][column+1])
        
        return dp[0][0]