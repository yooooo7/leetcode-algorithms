class Solution:
    def lengthOfLIS(self, nums: list) -> int:
        if len(nums) <= 1: return len(nums)
        
        opt = [0] * len(nums)
        opt[0] = 1
        
        for i in range(1, len(nums)):
            opt[i] = max([opt[k] if nums[k] < nums[i] else 0 for k in range(i)]) + 1
        
        return max(opt)