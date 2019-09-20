class Solution:
    # Another no. connected components question in disguise (see 323)
    # This time, we are already given an adjacency matrix, so no need to construct a graph like in 323
    # Do a dfs from each vertex if you haven't yet. DFS > BFS for no. conn comps
    # Complexity: Time O(m + n) Space O(m + n)
    def dfs(self, M, visited, curr):
        visited[curr] = True
        for next in range(len(M)):
            if M[curr][next] == 1 and not visited[next]:
                self.dfs(M, visited, next)
                
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        visited = [False for i in range(len(M))]
        circles = 0
        for student in range(len(M)):
            if not visited[student]:
                self.dfs(M, visited, student)
                circles += 1
        return circles