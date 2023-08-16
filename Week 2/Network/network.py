from collections import deque
global count
count = 0

def solution(n, computers):
    global count
    answer = 0
    visited = [False] * (n+1)
    graph = [[] for i in range(n+1)] 
    for i in range(1, n+1):
        pos = [p+1 for p in range(n) if computers[i-1][p]==1]
        graph[i] += [v for v in pos if i != v]
        
    for i in range(1, n+1):
        bfs(graph, i, visited)
        
    answer = count
    print(answer)

    return answer

def bfs(graph, start, visited):
    global count
    queue = deque()
    if visited[start] == False:
        visited[start] = True
        queue.append(start)
    
        while queue:
            v = queue.popleft()
            
            for i in graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    
        count += 1
    return 0