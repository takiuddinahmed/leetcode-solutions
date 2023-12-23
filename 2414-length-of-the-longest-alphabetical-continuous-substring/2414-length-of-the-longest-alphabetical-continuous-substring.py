class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        largest = 1
        
        count = 1
        prev_char = s[0]
        
        i = 1
        
        while i <len(s):
            if ord(s[i]) == ord(prev_char)+1:
                count += 1
                   
            else:
                if (count > largest):
                    largest =  count
                count = 1
            
            prev_char = s[i]
            i+= 1
        if (count > largest):
                    largest =  count
        return largest
        