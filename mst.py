Here's Python code for both Kruskal's and Prim's algorithms to find the Minimum Spanning Tree (MST).

Kruskal's Algorithm

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_v] < self.rank[root_u]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2]) # Sort edges by weight
    ds = DisjointSet(n)
    mst = []
    total_weight = 0
    for u, v, w in edges:
        if ds.union(u, v):
            mst.append((u, v, w))
            total_weight += w
            if len(mst) == n - 1:
                break
    return mst, total_weight

# Example usage:
edges = [(0, 1, 4), (0, 2, 3), (1, 2, 1), (1, 3, 2), (2, 3, 4)]
n = 4
mst, total_weight = kruskal(n, edges)
print("Kruskal MST:", mst)
print("Total weight:", total_weight)

Prim's Algorithm

import heapq

def prim(n, edges):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    mst = []
    visited = [False] * n
    min_heap = [(0, 0, -1)] # (weight, vertex, parent)
    total_weight = 0

    while min_heap and len(mst) < n - 1:
        w, u, parent = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        if parent != -1:
            mst.append((parent, u, w))
            total_weight += w
        for v, weight in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (weight, v, u))

    return mst, total_weight

# Example usage:
mst, total_weight = prim(n, edges)
print("Prim MST:", mst)
print("Total weight:", total_weight)

Want me to explain how either of these work or help you run one?