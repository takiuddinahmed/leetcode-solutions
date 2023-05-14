function majorityElement(nums: number[]): number {
    if(nums.length === 1){
        return nums[0]
    }
    const obj = {};
    
    for(let i=0;i<nums.length;i++){
        const num = nums[i]
        if(obj[num] !== undefined){
            obj[num] = obj[num]+1
            if(obj[num] >=( nums.length /2)){
                return num
            }
        }
        else {
            obj[num] = 1
        }
    }
};