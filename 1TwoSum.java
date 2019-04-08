// Solution to Leetcode #1, Two Sum

class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Our map will store the number in question as the key for quick access, and the index as the value.
        // Here, we give up space to save time. Space and time complexity are both O(n).
        Map<Integer, Integer> mySet = new HashMap<Integer, Integer>();
        int complement = 0;
        for(int i = 0; i < nums.length; i++) {
            // each pass, we have a complement to the current index that makes our target sum.
            complement = target - nums[i];
            // If we have previously seen the complement in the list, we found our answer.
            if(mySet.containsKey(complement)) {
                return new int[] {mySet.get(complement), i};
            }
            // If the complement is not in the list, store the current value for later.
            mySet.put(nums[i], i);
        }
        // Throw an error, since we know there should always be a solution to this problem, according to the
        // question guidelines.
        throw new IllegalArgumentException("No solution to this problem");
    }
}
