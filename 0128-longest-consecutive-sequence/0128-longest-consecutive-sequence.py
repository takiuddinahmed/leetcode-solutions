class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        
        largest = 0
        for num in nums:
            # check if the begining
            if not (num - 1) in nums:
                count = 1
                n = num
                while (n + 1) in nums:
                    count +=1
                    n +=1
                if count > largest:
                    largest = count
        return largest
                
        