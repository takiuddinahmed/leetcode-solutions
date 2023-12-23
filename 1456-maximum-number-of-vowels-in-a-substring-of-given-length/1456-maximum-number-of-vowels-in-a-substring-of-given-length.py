class Solution:
    
    def maxVowels(self, s: str, k: int) -> int:
        
        largest = 0
        
        count = 0
        
        i = 0
        while i < k:
            if s[i] == 'a' or s[i]=='e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
                count += 1
            i += 1
                
        largest = count
        
        
        
        while i < len(s) :
            
            # check new char 
            if s[i] == 'a' or s[i]=='e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
                
                count += 1
            
            # check old char
            if s[i-k] == 'a' or s[i-k]=='e' or s[i-k] == 'i' or s[i-k] == 'o' or s[i-k] == 'u':
                count -= 1
            
            if count > largest:
                largest = count

            i += 1
        return largest
        
        