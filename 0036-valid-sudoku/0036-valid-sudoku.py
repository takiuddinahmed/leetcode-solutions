class Solution:
    def check(self,nums):  
        freq = {}
        for num in nums:
            if num != '.' and num in freq:

                return False
            
            freq[num] = True
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # brute force
        
        cols = [[],[],[],[],[],[],[],[],[]]
        nines = [[],[],[],[],[],[],[],[],[]]
        
        i = 0
        
        while i < 9:
            row = board[i]
            
            # check row
            if not self.check(row):
                return False
            
            j = 0
            while j < 9:
                cols[j].append(row[j])
                # print(i,j,i//3,j//3,(i//3)*3 + (j//3))
                nines[(i//3)*3 + (j//3)].append(row[j])
                j += 1
            
            
            i += 1
        
        # check cols
        for col in cols:
            if not self.check(col):
                return False
        
        # check nine
        for nine in nines:
            if not self.check(nine):
                return False
        
        return True
            
                    
        
        