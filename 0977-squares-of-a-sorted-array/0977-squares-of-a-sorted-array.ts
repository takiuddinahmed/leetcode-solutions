function sortedSquares(nums: number[]): number[] {
    return nums.map(n=>n*n).sort((a,b)=>a-b)
};