from collections import deque
def solution(maps):
    answer = 0
    n = len(maps) #맵 세로 길이
    m = len(maps[0]) #맵 가로 길이

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1] #위, 아래, 왼, 오
    
    answer = bfs(maps, 0,0, dx, dy, n, m)
    print(answer)
    
    return answer

def bfs(graph, x, y, dx, dy, n, m):
    count = []
    route = [[0,0]]
    queue = deque()
    queue.append((x, y)) 
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                
                    if (graph[nx][ny] == 1):
                        route.append([nx, ny])
                        graph[nx][ny] += graph[x][y]
                        graph[x][y] = -1
                        queue.append((nx, ny))
                        
                if (nx == (n-1)) and (ny == (m-1)):
                    print(graph)
                    return max(map(max, graph))
                        
                else:
                    continue
    if graph[n-1][m-1] == 1: 
        return -1
    return max(map(max, graph))
 
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
solution(maps)