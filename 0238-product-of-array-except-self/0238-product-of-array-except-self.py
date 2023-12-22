class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix_arr = []
        postfix_arr = [1]*len(nums)
        
        i = 0
        mul = 1
        while i < len(nums):
            mul *= nums[i]
            prefix_arr.append(mul)
            i += 1
        i = len(nums) -1
        mul = 1
        while i>=0:
            mul *= nums[i]
            postfix_arr[i] = mul
            i -= 1
        
        final_arr = [postfix_arr[1]]
        
        i = 1
        
        while i < len(nums)-1:
            final_arr.append(prefix_arr[i-1] * postfix_arr[i+1])
            i+=1
            
        # final_arr[len(nums)- 1] = prefix_arr[len(nums) - 2]
        final_arr.append(prefix_arr[len(nums) - 2])
        return final_arr
        
            
            
        
        