class Solution:
    def check(self, nums):
        freq = {}
        for n in nums:
            if n in freq:
                return False
            freq[n] = True
        return True
    def checkValid(self, matrix: List[List[int]]) -> bool:
        
        cols = [[] for n in matrix]
        
        i = 0
        while i < len(matrix):
            row = matrix[i]
            if not self.check(row):
                return False
            
            # create col
            j = 0
            while j < len(row):
                cols[j].append(row[j])
                j +=1
            i += 1
        
        for col in cols:
            if not self.check(col):
                return False
        return True