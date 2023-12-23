class Solution:
    
    def isValid(self, s: str) -> bool:
        
        stack = []
        par = {')':'(',']': '[', '}': '{'}
        
        for char in s:
            
            if char in ('(','[', '{'):
                
                stack.append(char)
            
            elif char in (')',']','}'):
                if not len(stack) :
                    return False
                if stack.pop() != par[char]:
                    return False
        
        if len(stack) > 0:
            return False
        return True
        
        
        