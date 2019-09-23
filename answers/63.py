class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[0 for _ in range(N)] for _ in range(M)]
        
        for i in range(M-1, -1, -1):
            if obstacleGrid[i][-1] != 1:
                dp[i][-1] = 1
            else:
                break
        for j in range(N-1, -1, -1):
            if obstacleGrid[-1][j] != 1:
                dp[-1][j] = 1    
            else:
                break
        
        for row in range(M-2, -1, -1):
            for column in range(N-2, -1, -1):
                if obstacleGrid[row][column] != 1:
                    dp[row][column] = dp[row+1][column] + dp[row][column+1]
        
        return dp[0][0]