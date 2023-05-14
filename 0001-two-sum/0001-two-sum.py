class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementMap = dict()
        l = len(nums)
        for i in range(l):
            num = nums[i]
            complement = target - num
            if complement in complementMap:
                return [complementMap[complement], i]
            else:
                complementMap[num] = i