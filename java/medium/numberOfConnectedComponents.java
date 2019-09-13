class Solution {
    private void dfs(int curr, Map<Integer, List<Integer>> connected, boolean[] visited) {
        for (int next : connected.get(curr)) {
            if (!visited[next]) {
                visited[next] = true;
                dfs(next, connected, visited);
            }
        }
    }
    public int countComponents(int n, int[][] edges) {
        if (n == 0) {
            return 0;
        }
        boolean[] visited = new boolean[n];
        Map<Integer, List<Integer>> connected = new HashMap<>();
        for (int i = 0; i < n; i++) {
            connected.put(i, new ArrayList<Integer>());
        }
        for (int i = 0; i < edges.length; i++) {
            connected.get(edges[i][0]).add(edges[i][1]);
            connected.get(edges[i][1]).add(edges[i][0]);
        }
        int components = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i, connected, visited);
                components++;
            }
        }
        return components;
    }
}