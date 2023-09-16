func containsDuplicate(nums []int) bool {
    record := make(map[int]bool)
    
    for _, num := range nums {
        if _,ok := record[num]; ok {
            return true
        }
        record[num] = true
    }
    return false
}