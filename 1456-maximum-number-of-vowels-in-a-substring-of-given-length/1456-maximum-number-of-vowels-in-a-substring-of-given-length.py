class Solution:
    
    def maxVowels(self, s: str, k: int) -> int:
        
        largest = 0
        
        count = 0
        
        i = 0
        while i < k:
            if s[i] in ('a','e','i','o','u'):
                count += 1
            i += 1
                
        largest = count
        
        
        
        while i < len(s) :
            
            # check new char 
            if s[i] in ('a','e','i','o','u'):
                
                count += 1
            
            # check old char
            if s[i-k] in ('a','e','i','o','u'):
                count -= 1
            
            if count > largest:
                largest = count

            i += 1
        return largest
        
        