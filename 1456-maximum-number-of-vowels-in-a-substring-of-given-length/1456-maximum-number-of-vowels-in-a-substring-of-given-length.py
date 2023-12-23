class Solution:
    def check_vowel(self, char):
        if char in ('a','e','i','o','u'):
            return True
        return False
    
    def maxVowels(self, s: str, k: int) -> int:
        
        largest = 0
        i = k
        
        first_sub_string = s[i-k:i]
        count = 0
        
        for char in first_sub_string:
            if self.check_vowel(char):
                count += 1
                
        largest = count
        
        
        
        while i < len(s) :
            
            # check new char 
            if self.check_vowel(s[i]):
                
                count += 1
            
            # check old char
            if self.check_vowel(s[i-k]):
                count -= 1
            
            if count > largest:
                largest = count

            i += 1
        return largest
        
        