class Solution:
    # Using DFS to find Number of connected components
    # Complexity: Time O(m*n), Space O(m*n) absolute worst case, if the whole map is filled and you start at a corner
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs (i, j + 1)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count
    # If you cannot modify input
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        copy = [[grid[i][j] for j in range(len(grid[0]))] for i in range(len(grid))]
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(copy[0]) or copy[i][j] == '0':
                return
            copy[i][j] = '0'
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs (i, j + 1)
        count = 0
        for i in range(len(copy)):
            for j in range(len(copy[0])):
                if copy[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count