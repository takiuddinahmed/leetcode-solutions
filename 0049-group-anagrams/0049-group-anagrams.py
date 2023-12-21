class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}
        
        for word in strs:
            s = ''.join(sorted(word))
            
            if s in d:
                d[s].append(word)
            else:
                d[s] = [word]
        
        return list(d.values())
        