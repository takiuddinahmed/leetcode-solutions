class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        arr = [None]*(len(nums)+1)
        for key,value in freq.items():
            if arr[value]:
                arr[value].append(key)
            else:
                arr[value] = [key]
        
        count = 0
        res = []

        i = len(arr) - 1
        
        while i >= 0:
            if arr[i]:
                for n in arr[i]:
                    res.append(n)
                    count += 1
                    if count >= k:
                        return res
            i -= 1
        
        
        