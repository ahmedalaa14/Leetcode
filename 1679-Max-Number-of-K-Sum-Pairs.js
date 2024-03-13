/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxOperations = function(nums, k) {
    let map = new Map(), pairs = 0;
    for(let i = 0; i < nums.length; i++) {
        if(map.has(nums[i])) {
            map.set(nums[i], map.get(nums[i])+1);
        }
        else {
            map.set(nums[i],1);
        }
    }
    for(let i = 0; i < nums.length; i++) {
        if(map.get(nums[i])) {
            map.set(nums[i], map.get(nums[i])-1);
            if(map.get(k-nums[i])) {
                pairs++;
                map.set(k-nums[i], map.get(k-nums[i])-1);
            }
            else {
                map.set(nums[i], map.get(nums[i])+1);
            }
        }
    }
    return pairs;    
};