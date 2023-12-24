class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        arr =  sorted(freq.items(), key= lambda x: x[1], reverse=True)[:k]
        result = [ item[0] for item in arr ]
        return result
        
        # freq = {2:2, 3:1, 1:3}
        # arr = [(1,3),(2,2),(3,1)]
        
