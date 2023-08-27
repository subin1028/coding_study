from collections import deque
count = 0
vis = []
def bfs(graph, start, visited):
    global count
    queue = deque()
    if visited[start] == False:
        visited[start] = True
        queue.append(start)
    
        while queue:
            v = queue.popleft()
            if count == 0:
                vis.append(v)
            
            for i in graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True           
        count += 1
    return 0

count = 0
answer = 0

com = int(input())
e = int(input())

visited = [False] * (com+1) #방문 체크 리스트 생성
graph = [[] for _ in range(com+1)] #그래프 생성
for i in range(e):
    a, b = map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, com+1):
    bfs(graph, i, visited)
    if(i == com):
        print(len(vis) - 1)