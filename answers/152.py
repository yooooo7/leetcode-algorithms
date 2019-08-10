class Solution:
    # 解法超时
    # def maxProduct(self, nums: List[int]) -> int:
    #     N = len(nums)
    #     OPT = [0] * N
    #     OPT[0] = max(nums)
    #     Ms = nums.copy()
        
    #     for n in range(1, N):
    #         Ms = [Ms[i]*nums[i+n] for i in range(len(Ms) - 1)]
    #         curMax = max(Ms)
    #         OPT[n] = max(OPT[n - 1], curMax)
        
    #     return max(OPT)

    def maxProduct(self, nums) -> int:
        # N = len(nums)
        # OPT = [[0 for _ in range(2)] for _ in range(N)]
        # OPT[0][0], OPT[0][1], res = [nums[0]] * 3
        
        # for i in range(1, N):
        #     OPT[i][0] = max(OPT[i-1][0] * nums[i], OPT[i-1][1] * nums[i], nums[i])
        #     OPT[i][1] = min(OPT[i-1][0] * nums[i], OPT[i-1][1] * nums[i], nums[i])
            
        #     res = max(res, OPT[i][0])
        
        # return res

        ## 优化版
        N = len(nums)
        OPT = [[0 for _ in range(2)] for _ in range(2)]
        OPT[0][0], OPT[0][1], res = [nums[0]] * 3
        
        for i in range(1, N):
            x, y = i % 2, (i-1) % 2
            OPT[x][0] = max(OPT[y][0] * nums[i], OPT[y][1] * nums[i], nums[i])
            OPT[x][1] = min(OPT[y][0] * nums[i], OPT[y][1] * nums[i], nums[i])
            
            res = max(res, OPT[x][0])
        
        return res