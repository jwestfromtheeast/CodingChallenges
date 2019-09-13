# Leetcode 256
class Solution:
    # Optimal solution using dynamic programming
    # Can use O(1) space here by using the original array to cache previous result
    # In each spot, store the minimum of the previous two other colors (since cannot repeat color)
    def minCost(self, costs: List[List[int]]) -> int:
        length = len(costs)
        if length == 0:
            return 0
        for i in range(1, length):
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])
        return min(costs[length - 1][0], costs[length - 1][1], costs[length - 1][2])