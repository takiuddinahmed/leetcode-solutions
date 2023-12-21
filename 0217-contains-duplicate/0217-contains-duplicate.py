class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for num in nums:
            if num in freq:
                return True
            else:
                freq[num] = True
        return False
        