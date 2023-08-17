from collections import deque
def solution(maps):
    answer = 0
    n = len(maps) #맵 세로 길이
    m = len(maps[0]) #맵 가로 길이

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1] #위, 아래, 왼, 오
    
    print(bfs(maps, 0,0, dx, dy, n, m))
    
    return answer

def bfs(graph, x, y, dx, dy, n, m):
    count = 0
    route = [[0,0]]
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if ([nx, ny] != route[count-1]):
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                
                if graph[nx][ny] == 0:
                    continue
                
                if (graph[nx][ny] == 1):
                    route.append([nx, ny])
                    count += 1
                    queue.append((nx, ny))
                    break
                    
            else:
                continue
                
    return count, route
    

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

solution(maps)
# 한가지의 루트밖에 찾아내지 못함