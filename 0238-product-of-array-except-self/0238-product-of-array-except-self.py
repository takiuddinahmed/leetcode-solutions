class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        arr = [nums[0]]
        
        i = 0
        mul = 1
        while i < len(nums)-1:
            mul *= nums[i]
            arr.append(mul)
            i += 1
        
        i = len(nums) - 2
        mul = nums[len(nums)-1]
        while i > 0:
            arr[i] = mul * arr[i]
            mul *= nums[i]
            i-=1
        arr[0] = mul
        return arr
        
        
        
        
            
            
        
        