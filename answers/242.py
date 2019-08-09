class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        
        # 统计第一个字符串字母频率
        for l in s:
            if l not in dic:
                dic[l] = 1
            else:
                dic[l] += 1
        
        
        for l in t:
            if l not in dic:
                return False
            
            dic[l] -= 1
        
        
        for key in dic:
            if dic[key] != 0:
                return False
        
        return True