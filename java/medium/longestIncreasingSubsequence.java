// Leetcode 1143
class Solution {
    // O(m*n) time, O(m*n) space
    // Memoized Recursive solution
    private int lcsHelper(String a, String b, int i, int j, int[][] memo) {
        if (i == a.length() || j == b.length()) {
            return 0;
        }
        if (memo[i][j] != 0) {
            return memo[i][j];
        }
        if (a.charAt(i) == b.charAt(j)) {
            int curr = 1 + lcsHelper(a, b, i + 1, j + 1, memo);
            memo[i][j] = curr;
            return curr;
        }
        int curr = Math.max(lcsHelper(a, b, i, j + 1, memo), lcsHelper(a, b, i + 1, j, memo));
        memo[i][j] = curr;
        return curr;
    }
    public int longestCommonSubsequenceR(String text1, String text2) {
        if (text1.length() == 0) {
            return text2.length();
        }
        if (text2.length() == 0) {
            return text1.length();
        }
        int[][] memo = new int[text1.length()][text2.length()];
        return lcsHelper(text1, text2, 0, 0, memo);
    }
    
    // Iterative solution (always preferred if you can reach it)
    public int longestCommonSubsequence(String text1, String text2) {
        if (text1.length() == 0) {
            return text2.length();
        }
        if (text2.length() == 0) {
            return text1.length();
        }
        int[][] memo = new int[text1.length() + 1][text2.length() + 1];
        for (int i = 0; i < text1.length(); i++) {
            for (int j = 0; j < text2.length(); j++) {
                if (text1.charAt(i) == text2.charAt(j)) {
                    memo[i + 1][j + 1] = 1 + memo[i][j];
                } else {
                    memo[i + 1][j + 1] = Math.max(memo[i + 1][j], memo[i][j + 1]);
                }
            }
        }
        return memo[text1.length()][text2.length()];
    }
}