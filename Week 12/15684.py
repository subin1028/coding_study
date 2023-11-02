N,M,H=map(int,input().split()) #세로선, 가로선 개수, 가로선 위치

if M==0:
    print(0)
    exit(0)

radder=[[0]*N for _ in range(H)]
answer=4

def dfs(depth,nx,ny):
    global answer,radder
    if depth>3:
        return
    if depth>answer:
        return

    #먼저 현재 사다리 기준 다 내려가는지 보자
    flag=True
    for y in range(N): #세로선
        sy=y
        for x in range(H): #가로선
            # print(x,sy)
            if radder[x][sy]: #가로선 타고 움직이기
                sy+=1

            elif sy-1>=0:
                if radder[x][sy-1]: #가로선이 왼쪽에 위치
                    sy-=1 #가로선 타고 왼쪽으로 움직이기

        if not sy==y:
            flag=False
            break
    #다 맞는 번지에 내려왔다면 최소값 갱신
    if flag:
        answer=min(answer,depth)
        return
    
    #그게 아니라면 줄 추가
    else:
        for x in range(nx,H):#현재위치부터 가로줄 끝에서 2번째까지 만큼
            if x==nx:
                k=ny
            else:
                k=0
            for y in range(k,N-1):
                #현재 지점에 사다리가 놓여졌다면
                if radder[x][y]:
                    continue
                #이전 세로줄에 사다리가 놓여있다면(단, y-1>=0일떄만 체크)
                if y-1>=0 and radder[x][y-1]:
                    continue

                radder[x][y]=1
                dfs(depth+1,x,y)

for _ in range(M):
    a,b=map(int,input().split())
    if b==N:
        continue
    radder[a-1][b-1]=1

dfs(0,0,0)

if answer==4:
    print(-1)
    
else:
    print(answer)