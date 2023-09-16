function containsDuplicate(nums: number[]): boolean {
    const record = new Map<number, boolean>();
    
    for(const num of nums){
        if(record.get(num)){
            return true
        } else{
            record.set(num,true)
        }
    }
    return false
};