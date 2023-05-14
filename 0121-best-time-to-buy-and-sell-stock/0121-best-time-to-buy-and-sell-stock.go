func getMax(a int, b int) int {
    if(b>a){
        return b
    }
    return a
}
func maxProfit(prices []int) int {
    left := 0
    right := 1
    maxProfit := 0
    
    for (right < len(prices)){
        if(prices[right] > prices[left]){
            maxProfit = getMax(maxProfit, prices[right]-prices[left])
        } else {
            left = right
        }
        
        right ++
    }
    return maxProfit
    
}