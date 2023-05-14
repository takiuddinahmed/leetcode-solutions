function twoSum(nums: number[], target: number): number[] {
    const map = {}
    
    for (let i=0;i<nums.length;i++){
        const num = nums[i];
        if( map[target-num] !==undefined){
            return [map[target-num],i]
        }
        else {
            map[num] = i
        }
    }
};