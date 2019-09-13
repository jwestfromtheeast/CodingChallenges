// Leetcode 42
class Solution {
    // O(n) time O(1) space
    public int trap(int[] height) {
        if (height == null || height.length < 2) {
            return 0;
        }
        // Brute force would be for each index, iterate to the ends from that index, and find the max to the left and right of that index.
        // Add the minimum of the two sides minus the current height to the total, and repeat for each index.
        // Similar to Container with Most Water (11). Check that out first if you haven't
        //
        int trapped = 0;
        // Again with two pointers. This time, we need two extras, to hold the maxes as we go
        int leftMax = Integer.MIN_VALUE;
        int rightMax = Integer.MIN_VALUE;
        for (int left = 0, right = height.length - 1; left <= right;) {
            leftMax = Math.max(leftMax, height[left]);
            rightMax = Math.max(rightMax, height[right]);
            if (leftMax < rightMax) {
                trapped += leftMax - height[left];
                left++;
            } else {
                trapped += rightMax - height[right];
                right--;
            }
        }
        return trapped;
    }
}