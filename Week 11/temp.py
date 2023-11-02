from collections import deque

n,m = map(int,input().split())
ground = [list(map(int,input().split())) for i in range(n)]
dx= [0,0,-1,1]
dy= [1,-1,0,0]
year = 0 

def bfs(a,b):
    q = deque()
    q.append([a,b])
    visited[a][b] = 1
    chk = []
    while q:
        sea = 0
        x,y = q.popleft()
        for i in range(4):
            nx,ny = dx[i]+x,dy[i]+y
            if 0<=nx<n and 0<=ny<m:
                if not ground[nx][ny]:
                    sea += 1
                elif ground[nx][ny] and not visited[nx][ny]:
                    q.append([nx,ny])
                    visited[nx][ny] = 1
        chk.append([x,y,sea])
    for i,j,sea in chk:
        ground[i][j] = max(0,ground[i][j] - sea)
    return 1

ice = []
for i in range(n):
    for j in range(m):
        if ground[i][j]:
            ice.append((i,j))
    
while ice:
    visited = [[0]*m for _ in range(n)]
    dellist = []
    group = 0
    for i,j in ice:
        if ground[i][j] and not visited[i][j]:
            group += bfs(i,j)
        if ground[i][j] == 0:
            dellist.append((i,j))
    if group > 1:
        print(year)
        break
    ice =sorted(list(set(ice) - set(dellist)))
    year += 1

if group < 2:
    print(0)