class Solution:
    def maxProfit(self, prices: list) -> int:
        if not prices:
            return 0
        
        OPT = [[0 for _ in range(3)] for _ in range(len(prices))]
        OPT[0][0], OPT[0][1], OPT[0][2] = 0, -prices[0], 0
        
        res = 0
        
        for day in range(1, len(prices)):
            OPT[day][0] = OPT[day-1][0]
            OPT[day][1] = max(OPT[day-1][1], OPT[day-1][0] - prices[day])
            OPT[day][2] = OPT[day-1][1] + prices[day]
            
            res = max(res, OPT[day][2])
        
        return res