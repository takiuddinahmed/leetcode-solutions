class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_str =  "".join([char.lower() if char.isalnum() else ""  for char in s])
        
        i = 0
        l = len(new_str)
        if l < 2:
            return True

        while i < (l/2 + 1):
            if new_str[i] != new_str[l-i-1]:
                return False
            i += 1
        return True
        