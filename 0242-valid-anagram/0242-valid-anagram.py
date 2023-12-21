class Solution:
    def getFrequency(self, word: str) -> dict:
        freq = {}
        for char in word:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        return freq
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        s_freq = self.getFrequency(s)
        t_freq = self.getFrequency(t)
        
        
        for s_key in s_freq.keys():
            if s_key in t_freq:
                if s_freq[s_key] != t_freq[s_key]:
                    return False
            else:
                return False
        return True
        
        