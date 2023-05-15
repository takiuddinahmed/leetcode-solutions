func moveZeroes(nums []int)  {
    left:=0
    
    for right := 0; right<len(nums); right++ {
        if nums[right] != 0 && nums[left] ==0 {
            nums[left] = nums[right]
            nums[right] = 0
        }
        
        if nums[left] != 0 {
            left ++
        }
    }
}