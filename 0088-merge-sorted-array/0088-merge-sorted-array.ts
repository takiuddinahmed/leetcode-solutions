/**
 Do not return anything, modify nums1 in-place instead.
 */
function merge(nums1: number[], m: number, nums2: number[], n: number): void {
    let cur2 = 0
    let cur1 = 0
    
    while (cur1 < nums1.length){
        if(nums1[cur1] >= nums2[cur2]){
            for(let i=m;i>cur1;i--){
                nums1[i] = nums1[i-1];
            }
            m++
            nums1[cur1] = nums2[cur2]
            cur2++
        }
        else {
            cur1++
        }
        
    }

    while (cur2 < n) {
        nums1[nums1.length  - n + cur2] = nums2[cur2]
        cur2++
    }

    


};