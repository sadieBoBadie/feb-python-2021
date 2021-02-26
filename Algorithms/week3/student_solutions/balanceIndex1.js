const nums1 = [-9, -5, -2, 9, -16];
function balanceIndex(nums) {
    var remove_index = 0;
    if (nums.length % 2 != 0) {
        remove_index = Math.floor(nums.length / 2)
    }
    var sum = 0;
    var sum_half = 0;
    for (var i = 0; i < nums.length; i++) {
        sum = sum + nums[i]
    }
    sum = sum - nums[remove_index]
    for (i = 0; i < nums.length; i++) {
        sum_half = sum_half + nums[i]
        if (sum_half == sum / 2) {
            console.log(sum_half)
            return i + 1;
        }
    }
    return -1;
}
console.log(balanceIndex(nums1))