// Leetcode 771
class Solution {
    public int numJewelsInStones(String J, String S) {
        // Time: O(n + m) [O(n)] Space: O(n)
        // Naive solution here would be to use nested loops. The outer loop would iterate through
        // our stones, string S, then compare each stone in S to every jewel in J to see if the
        // stone is a jewel. We can trade time for space here by storing jewels in a Set.
        Set<Character> jewels = new HashSet<>();
        int numJewels = 0;
        for (char c : J.toCharArray()) {
            jewels.add(c);
        }
        for (char c : S.toCharArray()) {
            if (jewels.contains(c)) {
                numJewels++;
            } 
        }
        return numJewels;
    }
}