// Solution to Leetcode #1, Two Sum

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> mySet = new HashMap<Integer, Integer>();
        int complement = 0;
        for(int i = 0; i < nums.length; i++) {
            complement = target - nums[i];
            if(mySet.containsKey(complement)) {
                return new int[] {mySet.get(complement), i};
            }
            mySet.put(nums[i], i);
        }
        throw new IllegalArgumentException("No solution to this problem");
    }
}
