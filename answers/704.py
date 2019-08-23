class Solution:
    def search(self, nums: list, target: int) -> int:
        n = len(nums)
        return bs_r(nums, target, 0, n - 1)

    
def bs_r(nums, target, low, high):
    if low > high:
        return -1

    mid = (low+high) // 2

    if nums[mid] == target:
        return mid

    if nums[mid] > target:
        return bs_r(nums, target, low, mid - 1)
    else:
        return bs_r(nums, target, mid + 1, high)