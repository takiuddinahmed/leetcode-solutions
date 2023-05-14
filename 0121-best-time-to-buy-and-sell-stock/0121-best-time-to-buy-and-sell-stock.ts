function getMax (a:number, b: number): number{
    if (b>a) return b;
    return a
}

function maxProfit(prices: number[]): number {
    let left = 0, right = 1;
    let maxProfit = 0;
    
    while(right<prices.length){
        if(prices[left] < prices[right]){
            maxProfit = getMax(maxProfit, prices[right] - prices[left])
        }
        else {
            left = right
        }
        right = right + 1
    }
    return maxProfit
};