/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    let n = nums.length;
    
    let countPositives = segregate(nums);
    
    for (let i = 0; i < countPositives; i++) {
        let num = Math.abs(nums[i]);
        if (num <= countPositives) {
            let index = num - 1;
            nums[index] = -Math.abs(nums[index]);
        }
    }
    
    for (let i = 0; i < countPositives; i++) {
        if (nums[i] > 0) {
            return i + 1;
        }
    }
    return countPositives + 1;
    
    function segregate(nums) {
        let j = 0;
        for (let i = 0; i < n; i++) {
            if (nums[i] > 0) {
                let temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                j++;           
            }
        }
        return j;
    }
};