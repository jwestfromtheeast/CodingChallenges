// Leetcode 283
class Solution {
    public void moveZeroes(int[] nums) {
        // Always address edges cases such as invalid input
        // Naive solution: use another array and fill with non-zeroes as you go
        // Then, add zeroes at the end. However, we can do this with constant space!
        if (nums == null || nums.length == 0) {
            return;
        }
        // As you move through the array, count the zeroes
        // Move each non-zero up by the amount of zeroes seen so far
        int zeroes = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                zeroes++;
            } else {
                nums[i - zeroes] = nums[i];
            }
        }
        // All non-zeroes moved up, so make the remaining indexes equal to zero
        for (int i = nums.length - zeroes; i < nums.length; i++) {
            nums[i] = 0;
        }
    }
}