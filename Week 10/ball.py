N, M = map(int, input().split()) #맵 크기 받기
board = [list(input().rstrip()) for _ in range(N)]  #맵 받기
dx = [-1, 1, 0, 0]  # 움직임
dy = [0, 0, -1, 1] 
queue = []
#방문지 확인
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

def pos_init():
    rx, ry, bx, by = 0, 0, 0, 0 #위치 변수
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R': #빨간 구슬 위치 찾기
                rx, ry = i, j
            elif board[i][j] == 'B': #파란 구슬 위치 찾기
                bx, by = i, j
    queue.append((rx, ry, bx, by, 1)) #현재 위치와 움직임 횟수 넣어주기
    #제일 처음에 쓸 함수라 1 들어감
    visited[rx][ry][bx][by] = True

def move(x, y, dx, dy):
    cnt = 0  # 이동 수 변수
    # 다음이 벽이거나 현재가 구멍일 때까지
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def solution():
    pos_init()  # 초기화
    while queue:  #BFS
        rx, ry, bx, by, depth = queue.pop(0)
        if depth > 10:  # 이동 횟수가 10을 초과하면
            break # 끝내기
        for i in range(4):  #상하좌우
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])  #빨간공 움직이기
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])  #파란공 움직이기
            if board[nbx][nby] != 'O':  #파란 공이 구멍과 만나지 않고
                if board[nrx][nry] == 'O':  #빨간공이 구멍과 만났으면
                    print(depth) #답 출력
                    return
                if nrx == nbx and nry == nby:  #두 공이 같은 위치라면
                    if rcnt > bcnt:  # 이동거리가 많은 것을
                        nrx -= dx[i]  # 한 칸 뒤로
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                # 방문한 곳인지 확인
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    # 다음 depth 탐색 위한 queue
                    queue.append((nrx, nry, nbx, nby, depth+1))
    print(-1)  # 실패 시

solution()