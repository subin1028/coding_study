from collections import deque
def solution(maps):

    n = len(maps) #맵 세로 길이
    m = len(maps[0]) #맵 가로 길이

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1] #위, 아래, 왼, 오
    
    check = [[-1 for _ in range(m)] for _ in range(n)]
   

    queue = deque()
    queue.append([0, 0]) 
    
    check[0][0] = 1
    
    while queue:
       y,x = queue.popleft()
       
       for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= ny < n and 0 <= nx < m and (maps[ny][nx] == 1):

                if check[ny][nx] == -1:
                    check[ny][nx] = check[y][x] + 1
                    queue.append([ny, nx])
   
    return check[-1][-1]
 
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
solution(maps)