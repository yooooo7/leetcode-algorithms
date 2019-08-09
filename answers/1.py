class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        
        for idx, num in enumerate(nums):
            another_num = target - num
            if another_num in dic:
                return [dic[another_num], idx]
            else:
                dic[num] = idx
        
        return []