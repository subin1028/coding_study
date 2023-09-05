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
       x, y = queue.popleft()
       
       for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and (maps[nx][ny] == 1):

                if check[nx][ny] == -1:
                    check[nx][ny] = check[x][y] + 1
                    queue.append([nx, ny])
   
    print(check)
    return check[-1][-1]
 
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
solution(maps)