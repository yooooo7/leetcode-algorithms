class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        if n <= 1:
            return s
        
        dp = [[False for _ in range(n)] for _ in range(n)]
        longest_substring = s[0]
        
        for i in range(n):
            dp[i][i] = True
        
        for left in range(n - 2, -1, -1):
            for right in range(left + 1, n):
                if left + 1 <= right - 1:
                    dp[left][right] = s[left] == s[right] and dp[left+1][right-1]
                else:
                    dp[left][right] = s[left] == s[right]
        
                if dp[left][right] and (right - left + 1) > len(longest_substring):
                    longest_substring = s[left: right + 1]

        return longest_substring