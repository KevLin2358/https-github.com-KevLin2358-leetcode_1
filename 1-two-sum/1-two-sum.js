/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
     let hash = {};
    
    for(let i = 0; i < nums.length; i++){
        if(!hash[nums[i]]) hash[nums[i]] = i;
    }
    
    for(let i = 0; i < nums.length; i++){
        let sub = target - nums[i];
        if(hash[sub] && hash[sub] !== i)return [hash[sub],i]
    }
};