/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    if (nums.length < 1) return [];
    
    let result = [nums[0]];
    
    for (let i = 1; i < nums.length; i++) {
        let sum = result[i-1] + nums[i];
        result.push(sum);
    }
    return result;
};