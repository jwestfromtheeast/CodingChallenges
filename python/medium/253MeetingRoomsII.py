# Leetcode 253
class Solution:
    # Here: break the 2d array into 2 1d arrays of start and end times, sort them
    # Now, if a meeting ever starts before one ends, we know we need an extra room
    # Compare all necessary starts and ends. If a conflict, DO NOT increment the end pointer. Always inc the start pointer
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        start, end = [], []
        for x in intervals:
            start.append(x[0])
            end.append(x[1])
        start.sort()
        end.sort()
        rooms = e = 0
        for s in range(len(intervals)):
            if start[s] < end[e]:
                rooms += 1
            else:
                e += 1
        return rooms