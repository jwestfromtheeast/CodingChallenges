// Leetcode 11
class Solution {
    public int maxArea(int[] height) {
        // Time: O(n) Space: O(1)
        // Always consider edge cases
        if (height == null || height.length < 2) {
            return 0;
        }
        // Brute force solution would be nested for loops to compare each index of the array to every other O(n^2)
        int maxi = 0;
        // Iterate through as such: have a left and right pointer on the edges of the array
        // Each time, the area we can fill will be the height of the smaller side * the distance betweeen right and left (area of rectangle)
        // Then, move the smaller pointer by one, to hope to find a larger solution
        for (int left = 0, right = height.length - 1; left <= right;) {
            if (height[left] < height[right]) {
                maxi = Math.max(maxi, height[left] * (right - left));
                left++;
            } else {
                maxi = Math.max(maxi, height[right] * (right - left));
                right--;
            }
        }
        return maxi;
    }
}