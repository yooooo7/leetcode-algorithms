class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length <= 1: return s
        
        dp = [[False for _ in range(length)] for _ in range(length)]
        
        longest_length = 1
        result = s[0]
        
        for r in range(1, length):
            for l in range(r):
                if s[l] == s[r] and (l+1 >= r-1 or dp[l+1][r-1]):
                    dp[l][r] = True
                    
                    cur_length = r - l + 1
                    if cur_length > longest_length:
                        longest_length = cur_length
                        result = s[l: r+1]
        
        return result