from collections import deque


class Solution:
    # Time Complexity: O(mn) time, O(mn) space
    # Logic: Here, we want to use a dfs or bfs for traversal. Since a recursive dfs will potentially stack overflow,
    # we will use a bfs by using a queue. This problem becomes simple with that idea in mind, and when following the
    # problem statement that any region on a border is not surrounded, and thus must remain as "O"s. So, let's go
    # through the graph and mark any region of O's originating from a boundary (and thus not surrounded) with a new character (not X or O).
    # Then, we can go back at the end and replace any region of our special character with O's, and the rest with X's, and this will satisfy the problem.
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        if m <= 2 or n <= 2:
            return

        # Place all of the boundary coordinates in the queue. Use a tuple x, y pair to store the coordinates.
        q = deque()
        for i in range(m):
            q.append((i, 0))
            q.append((i, n - 1))
        for j in range(n):
            q.append((0, j))
            q.append((m - 1, j))

        # For any boundary that is an O, we want to mark that region. so, mark it with any char and perform a bfs by adding its neighbors to the queue.
        while q:
            i, j = q.popleft()
            if 0 <= i < m and 0 <= j < n and board[i][j] == "O":
                board[i][j] = "Z"
                q.append((i - 1, j))
                q.append((i, j - 1))
                q.append((i + 1, j))
                q.append((i, j + 1))

        # Go back and replace any marked regions with O's, and the rest with X's. This will fill in any surrounded regions.
        for i in range(m):
            for j in range(n):
                if board[i][j] == "Z":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
