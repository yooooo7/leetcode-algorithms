# 二分法
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        
        n = x
        high = n
        low = 0
        
        while low <= high:
            mid = (low+high) // 2
            
            if mid**2 == x:
                return mid
            
            if mid**2 > x:
                high = mid - 1
            else:
                if mid == n or (mid + 1)**2 > x:
                    return mid
                else:
                    low = mid + 1
        
        return -1