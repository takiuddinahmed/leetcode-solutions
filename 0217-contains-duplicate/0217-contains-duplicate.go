func containsDuplicate(nums []int) bool {
    record := map[int]bool{}
    
    // for _, num := range nums {
    //     if _,ok := record[num]; ok {
    //         return true
    //     }
    //     record[num] = true
    // }
    for i:=0;i<len(nums);i++{
        if _, ok:= record[nums[i]]; ok {
            return true
        }
        record[nums[i]] = true
    }
    return false
}