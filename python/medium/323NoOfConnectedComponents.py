class Solution:
    # Classic graph problem. DFS is great at finding this
    # Simply have an array of visited so far, and visit more if not so
    # After each dfs called from our main completes, inc the no. conn comp
    # Complexity of DFS is O(V + E)
    # Complexity: Time O(n + m) Space O(n^2) (if every node connected to every other, far worst case. O(n + m) tighter)
    # Where n is the number of vertices and v is the number of edges
    def dfs(self, graph, visited, i) -> None:
        visited[i] = True
        for next_node in graph[i]:
            if not visited[next_node]:
                self.dfs(graph, visited, next_node)
           
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return n
        graph = {i: [] for i in range(n)}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        visited = [False for i in range(n)]
        conn_comp = 0
        for curr in graph:
            if not visited[curr]:
                self.dfs(graph, visited, curr)
                conn_comp += 1
        return conn_comp