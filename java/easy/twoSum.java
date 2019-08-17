// Leetcode 1!
class Solution {
    // Naive solution: nested for loop. Compare each element of the array with every other element
    // Poor time complexity of O(n^2)

    // Better solution and common trend in array problems: Trade TIME for SPACE
    // As you move through the array, store each element in a Map
    // At each index, you know what other number you need besides the current index to make the target sum (subtraction)
    // See if the complement (sum - current number) is in the map. if so, you have your pair!
    public int[] twoSum(int[] nums, int target) {
        if (nums.length == 0 || nums == null) {
          throw new IllegalArgumentException("Invalid input");  
        }
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[] {map.get(complement), i};
            }
            map.put(nums[i], i);
        }
        throw new IllegalArgumentException("No answer found!");
    }
}