// Leetcode 53
class Solution {
    // O(n) time, O(1) space
    // Initial solution with n space
    public int maxSubArrayNSpace(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int[] sums = new int[nums.length];
        sums[0] = nums[0];
        int max = nums[0];
        for (int i = 1; i < nums.length; i++) {
            sums[i] = Math.max(nums[i], nums[i] + sums[i - 1]);
            max = Math.max(max, sums[i]);
        }
        return max;
    }
    
    // Since you only ever access the previous array index, can use a single int rather than an array
    public int maxSubArray(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int currMax = nums[0];
        int max = nums[0];
        for (int i = 1; i < nums.length; i++) {
            currMax = Math.max(nums[i], currMax + nums[i]);
            max = Math.max(max, currMax);
        }
        return max;
    }
}