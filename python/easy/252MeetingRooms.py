# Leetcode 252
class Solution:
    # Use sort and lambda to sort meetings by the time they start
    # If a meeting ever starts before another the previous ends, cannot attend all
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda x: x[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True