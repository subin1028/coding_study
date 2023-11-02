from collections import deque
from itertools import product

h, w = list(map(int, input().split()))
room = []
wh_num = 0 #전체 0 개수
ct = [] #카메라 위치, 종류, 감시 구역

for i in range(h):
    room.append(list(map(int,input().split(' '))))
    
for i in range(h):
    for j in range(w):
        if 1 <= room[i][j] <= 5:
            ct.append([i, j, room[i][j], []]) #카메라 위치, 종류, 감시 구역
            
        elif room[i][j] == 0:
            wh_num += 1
            
def security(ct_num, cct): #방향, (카메라위치, 종류)
    for direction in ct_num:
        area = [] #감시 가능 구역
        for dh, dw in direction: #이동방향
            q = deque()
            q.append((cct[0], cct[1]))
            while q:
                ch, cw = q.popleft() #카메라 위치
                nh = ch + dh #현재 위치
                nw = cw + dw
  
                if 0 <= nh < h and 0 <= nw < w: #방을 넘지 않으면
                    if room[nh][nw] == 6: #벽이면
                        break
                    else:
                        q.append([nh, nw])
                        if room[nh][nw] == 0:
                            area.append([nh, nw])
                            
        cct[3].append(area) #감시가능 구역 넣기
        print(area)
                    

ct1 = [[[-1,0]],[[1,0]],[[0,-1]],[[0,1]]] #한방향
ct2 = [[[-1,0],[1,0]],[[0,-1],[0,1]]] #180도
ct3 = [[[-1,0],[0,-1]], [[-1,0],[0,1]], [[1,0],[0,-1]], [[1,0],[0,1]]] #90도
ct4 = [[[-1,0],[1,0],[0,-1]], [[-1,0],[1,0],[0,1]], [[-1,0],[0,-1],[0,1]],[[1,0],[0,-1],[0,1]]] #3구역
ct5 = [[[-1,0],[1,0],[0,-1],[0,1]]] #동서남북

for cct in ct:
    cnh, cnw, num = cct[:3]
    if num == 1:
        security(ct1, cct)
    elif num == 2:
        security(ct2, cct)
    elif num == 3:
        security(ct3, cct)
    elif num == 4:
        security(ct4, cct)
    elif num == 5:
        security(ct5, cct)
        
areas = [] #감시한 구역 합치기
for cct in ct:
    areas.append(cct[3])
    
print(list(product(areas)))
#[([[[1, 2], [0, 2]], [[3, 2]], [[2, 1], [2, 0]], [[2, 3]]],)]

max_blind = 64
for i in product(*areas):
    secure = set()
    for j in i:
        for r,c in j:
            secure.add((r,c))
            
    if max_blind > wh_num - len(secure):
        max_blind = wh_num - len(secure)
        
print(max_blind)
        