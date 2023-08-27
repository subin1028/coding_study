from collections import deque

#정점개수, 간선개수, 시작정점
v, e, s = map(int, list(input().split(" ")))

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

visited_d = [False] * (v+1)
visited_b = visited_d.copy()
graph = [[] for _ in range(v+1)]

for i in range(e):
    a,b = map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

dfs(graph, s, visited_d)
print()
bfs(graph, s, visited_b)