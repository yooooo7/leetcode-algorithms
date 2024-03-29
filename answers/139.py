class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        n = len(s)
        
        dp = [False for _ in range(n + 1)]
        dp[0] = True
        
        for i in range(1, n+1):
            for j in range(i - 1, -1, -1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        
        return dp[-1]