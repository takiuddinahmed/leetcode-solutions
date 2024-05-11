class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        
        i = 0
        s = ""
        while i < n:
            s += word1[i] + word2[i]
            i += 1
        s += word1[n:] + word2[n:]
        return s
            