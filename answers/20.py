class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        blacket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        stack = []
        
        for b in s:
            if b in blacket_map:
                if len(stack) == 0:
                    return False
                
                cur_left = stack.pop(-1)
                if blacket_map[b] != cur_left:
                    return False
                
            else:
                stack.append(b)
        
        return len(stack) == 0