class Solution:
    # Bottom-up DP solution. Cache prev results
    # Complexity: O(n^2) time, O(n^2) space
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1 for j in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[-1][-1]