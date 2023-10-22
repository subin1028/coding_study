N,M=map(int,input().split())
graph=[]
bx, by, rx, ry = 0,0,0,0

dx=[0,0,1,-1]
dy=[1,-1,0,0]

for i in range(N):
    data=list(input().rstrip()) #맵 한줄씩 받기
    graph.append(data) #그래프에 넣기

    for j in range(M): 
        if data[j]=='B': #파란색 공 위치 저장
            bx, by=i, j
        if data[j]=='R': #빨간색 공 위치 저장
            rx, ry=i, j

def move_ball(x,y,d):
    cnt=0
    while graph[x+dx[d]][y+dy[d]]!='#' and graph[x][y]!='O': #구멍이나 맵 끝이 아니면
        x+=dx[d] #이동
        y+=dy[d]
        cnt+=1

    return x,y,cnt

answer=11

def dfs(bx,by,rx,ry,time):
    global answer
    if time>10:
        return # 10번 이상 움직였으면 멈추기

    b_cnt=0 #이동횟수 들어갈 변수
    r_cnt=0
    
    #상하좌우 이동
    for d in range(4):
        nbx,nby,b_cnt=move_ball(bx,by,d)
        nrx,nry,r_cnt=move_ball(rx,ry,d)

        #파란색이 들어가면 실패
        if graph[nbx][nby]=='O':
            return
        #빨간색이 홀에 들어가면 게임 끝
        if graph[nrx][nry]=='O':
            answer=min(answer,time)
            return

        # 빨간색과 파란색이 서로 겹칠 경우
        if nbx==nrx and nby==nry:
            if b_cnt>r_cnt:
                nbx-=dx[d]
                nby-=dy[d]
            elif b_cnt<r_cnt:
                nrx-=dx[d]
                nry-=dy[d]

        dfs(nbx,nby,nrx,nry,time+1)

time=1
dfs(bx,by,rx,ry,time)

if answer==11:
    print(-1)
else:
    print(answer)