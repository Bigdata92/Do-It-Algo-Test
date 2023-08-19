# 11724
# dfs
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
for tmp1 in graph[1:]:
    if not len(tmp1):
        cnt += 1

def dfs(graph, start, visited):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

for idx1 in range(1, n+1):
    if not visited[idx1] and len(graph[idx1]) != 0:
        dfs(graph, graph[idx1][0], visited)
        cnt += 1
        if visited[1:].count(True) == n:
            break
print(cnt)

# bfs
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

for idx1 in range(1, n+1):
    if not visited[idx1] and len(graph[idx1]) != 0:
        bfs(graph, graph[idx1][0], visited)
        cnt += 1
        if visited[1:].count(True) == n:
            break
print(cnt)