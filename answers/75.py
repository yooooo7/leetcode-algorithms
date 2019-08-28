class Solution:
    def sortColors(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 申请计数数组
        counter = [0] * 3
        
        # 计算每个元素个数
        for num in nums:
            counter[num] += 1
        
        # 累加
        for i in range(1, len(counter)):
            counter[i] += counter[i-1]
        
        # 申请临时数组
        r = [0] * len(nums)
        
        # 计算排序(保证时间复杂度为O(n))
        for num in nums:
            idx = counter[num] - 1
            r[idx] = num
            counter[num] -= 1
        
        # 替换原数组(要求原地排序，但是其实并不是原地排序)
        for i in range(len(nums)):
            nums[i] = r[i]