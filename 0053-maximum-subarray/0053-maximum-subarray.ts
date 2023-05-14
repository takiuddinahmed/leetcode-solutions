function maxSubArray(nums: number[]): number {
    let maxSub = nums[0];
    let curSub = 0;
    
    for (let i=0;i<nums.length;i++){
        const num = nums[i];
        curSub = Math.max(num,curSub+num);
        maxSub = Math.max(maxSub, curSub)
    }
    return maxSub
};