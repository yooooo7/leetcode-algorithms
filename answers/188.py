class Solution:
    def greedy(self, prices):
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res
    
    def maxProfit(self, k: int, prices: list) -> int:
        if not prices or not k: return 0
        
        day_nums = len(prices)
        
        if k > day_nums // 2: return self.greedy(prices)
        
        opt = [[[0 for _ in range(2)] for _ in range(k + 1)] for _ in range(day_nums)]
        
        opt[0][0][0], opt[0][0][1] = 0, -prices[0]
        
        for i in range(1, k + 1):
            opt[0][i][0], opt[0][i][1] = float("-inf"), float("-inf")
            
        for day in range(1, day_nums):
            opt[day][0][0] = 0
            opt[day][0][1] = max(opt[day-1][0][1], opt[day-1][0][0] - prices[day])
        
        for day in range(1, day_nums):
            for time in range(1, k + 1):
                opt[day][time][0] = max(opt[day-1][time][0], opt[day-1][time-1][1] + prices[day])
                opt[day][time][1] = max(opt[day-1][time][1], opt[day-1][time][0] - prices[day])
        
        return max([opt[day_nums - 1][time][0] for time in range(k + 1)])