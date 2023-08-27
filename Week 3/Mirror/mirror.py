from collections import deque

n, m = map(int, input().split(" "))
maps = [[] for _ in range(n)]

for i in range(0, n):
    a = input()
    for num in a:
        maps[i].append(int(num))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] #위, 아래, 왼, 오

check = [[-1 for _ in range(m)] for _ in range(n)] #방문 여부 및 방문 개수

queue = deque()
queue.append([0, 0]) 

check[0][0] = 1

while queue:
    x, y = queue.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and (maps[nx][ny] == 1):
            if check[nx][ny] == -1: #방문하지 않았으면
                check[nx][ny] = check[x][y] + 1 
                queue.append([nx, ny])

print(check[-1][-1]) #가장 마지막 방문 위치에 저장된 개수 출력