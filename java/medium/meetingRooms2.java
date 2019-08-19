// Leetcode 253
import java.util.*;
class Solution {
    public int minMeetingRooms(int[][] intervals) {
        // Break up meetings into the start and end times
        int[] start = new int[intervals.length];
        int[] end = new int[intervals.length];
        for (int i = 0; i < intervals.length; i++) {
            start[i] = intervals[i][0];
            end[i] = intervals[i][1];
        }
        // Sort accordingly
        Arrays.sort(start);
        Arrays.sort(end);
        int rooms = 0;
        int e = 0;
        // Each time a meeting starts before another ends, you need an extra room
        // If a meeting doesn't start before another ends, look at the next end
        for (int i = 0; i < intervals.length; i++) {
            if (start[i] < end [e]) {
                rooms++;
            } else {
                e++;
            }
        }
        return rooms;
    }
}