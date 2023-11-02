from collections import deque
# import numpy as np
M, N, H = list(map(int, input().split())) #M은 가로칸, N은 세로칸, H는 쌓아올려지는 수

box = [[] for _ in range(H)]

for i in range(H):
    for j in range(0, N):
        box[i].append(list(map(int,input().split()))) #1 익은, 0 안 익은, -1 없는
    
visited = [[[False]*M for _ in range(N)] for _ in range(H)]

x = [0, 0, 1, -1, 0, 0]
y = [1, -1, 0, 0, 0, 0]
z = [0, 0, 0, 0, 1, -1]
#위 아래 오른쪽 왼쪽 앞 뒤

queue = deque()
count = 0

for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1 and visited[i][j][k] == False:
                queue.append([i, j, k])
                visited[i][j][k] = True

def bfs():
    while(queue):
        h, n, m = queue.popleft()
        
        for i in range(6):
            nx = x[i] + h
            ny = y[i] + n 
            nz = z[i] + m
            
            if nx < 0 or nx >= H or ny < 0 or ny >= N or nz < 0 or nz >= M:
                continue
            
            if box[nx][ny][nz] == 0 and visited[nx][ny][nz] == False:
                queue.append([nx, ny, nz])
                box[nx][ny][nz] = box[h][n][m] + 1
                visited[nx][ny][nz] = True
                
bfs()

# np3 = np.array(box)
# if 0 in np3:
#     print(-1)
# else:
#     max_value = np.max(np3)
#     print(max_value-1)

for i in box:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit()
                
        count = max(count, max(j))
                
print(count - 1)
                

