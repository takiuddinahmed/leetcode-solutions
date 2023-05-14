function maxSubArray(nums: number[]): number {
    let maxSub = nums[0];
    let curSub = 0;
    
    for (let i=0;i<nums.length;i++){
        const num = nums[i];
        curSub = maxVal(num,curSub+num);
        maxSub = maxVal(maxSub, curSub)
    }
    return maxSub
};

function maxVal(a:number, b:number): number{
    if (b>a) return b;
    return a
}