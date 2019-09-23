class Solution:
    def maxSubArray(self, nums: list) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        
        for i in range(1, n):
            dp[i] = max(nums[i], nums[i]+dp[i-1])
        
        return max(dp)