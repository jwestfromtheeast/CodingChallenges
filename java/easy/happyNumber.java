// Leetcode 202
class Solution {
    private boolean isHappyR(int n, Set<Integer> prev) {
        if (n == 1) {
            return true;
        }
        int newNum = 0;
        while (n > 0) {
            int next = n % 10;
            newNum += next * next;
            n /= 10;
        }
        if (prev.contains(newNum)) {
            return false;
        }
        prev.add(newNum);
        return isHappyR(newNum, prev);
    }
    public boolean isHappyR(int n) {
        return isHappy(n, new HashSet<Integer>());
    }
    
    public boolean isHappy(int n) {
        Set<Integer> set = new HashSet<>();
        while (n != 1) {
            int nextNum = 0;
            while (n > 0) {
                int next = n % 10;
                nextNum += next * next;
                n /= 10;
            }
            if (set.contains(nextNum)) {
                return false;
            }
            set.add(nextNum);
            n = nextNum;
        }
        return true;
    }
}