class Solution:
    # Complexity: O(mn) time, O(mn) space
    # Logic: First, set all cells to infinity, since we are finding minimums. Work backward, from the princess back to the start (top-left),
    # and calculate the minimum hp we need at each location to get to the end from there. Build upon previous solutions for each new square
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon or not dungeon[0]:
            return
        # Initialize here
        dp = [[float("inf") for j in range(len(dungeon[0]) + 1)]
              for i in range(len(dungeon) + 1)]
        # Base case for cells adjacent to Princess: If the number is negative, you need 1 + the value in the cell. If it is positive, you need 1 hp
        dp[-1][-2] = dp[-2][-1] = 1
        # Iterate backwards
        for i in range(len(dungeon) - 1, -1, -1):
            for j in range(len(dungeon[0]) - 1, -1, -1):
                # The other key line: Calculating the current square based on the dungeon and previous dp squares. We look at the next two squares and take the min of them - the current dungeon square
                # , because a larger negative value here represents a larger hp pool. Then, take the max of that and 1, because the minimum hp we can take and survive is 1 (not 0 or a negative).
                dp[i][j] = max(
                    min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)
        return dp[0][0]
