import java.util.*;
// Leetcode 252
class Solution {
    public boolean canAttendMeetings(int[][] intervals) {
        // O(nlogn) time complexity, O(1) space
        if (intervals == null || intervals.length < 2) {
            return true;
        }
        // Sort the arrays according to the first index of each (start of meeting)
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        for (int i = 1; i < intervals.length; i++) {
            // If a meeting ever starts before the previous one ends, you cannot attend all
            if (intervals[i][0] < intervals[i - 1][1]) {
                return false;
            }
        }
        return true;
    }
}