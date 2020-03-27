from collections import deque  # Necessary for BFS
from collections import defaultdict  # Necessary for Adjacency List

vis = [0]*1000000              # Visited array to keep track of visited nodes

graph = defaultdict(list)      # Adjacency list of neighbours of each node

def DFS(v):                    # Recursice DFS Function
	print(v)
	if vis[v]:
		return
	vis[v] = 1
	for u in graph[v]:
		if not vis[u]:
			DFS(u)             # Note that stack size in Python is limited and so, number of nodes should'nt exceed 1000

def BFS(v):                    # Iterative BFS Function
	queue = deque([v])
	vis = [0]*1000000
	vis[v] = 1
	while queue:
		v = queue.popleft()
		print(v)
		for u in graph[v]:
			if not vis[u]:
				queue.append(u)
				vis[u] = 1

n, m = map(int, input().split())

for _ in range(m):
	u, v = map(int, input().split())
	graph[u].append(v)            # Bidirectional Edges
	graph[v].append(u)

DFS(1)
BFS(1)
