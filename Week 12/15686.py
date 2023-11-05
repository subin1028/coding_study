from itertools import combinations
from collections import deque
N,M = map(int, input().split())

village = [list(map(int, input().split())) for _ in range(N)]
#0 빈칸, 1 집, 2 치킨집
ch_max = 13
home = []
chicken = []

for i in range(N):
    for j in range(N):
        if village[i][j] == 1:
            home.append([i,j])
            
        elif village[i][j] == 2:
            chicken.append([i,j])

combi_chicken = deque(list(combinations(chicken, M)))
wh_dis = 0     
max_dis = N * 2     

total = 1e9

while combi_chicken:
    wh_dis = 0
    chickens = combi_chicken.popleft()
    for r,c in home: #집 돌아
        max_dis = N * 2 
        for cr, cc in chickens: #집마다 치킨 집 거리 계산해
            dis = abs(r-cr) + abs(c-cc)
            max_dis = min(max_dis, dis) #제일 작은 거리 구해     
            # print(f'{(r,c)}번째 집 {cr, cc}번째 치킨집: 최소: {max_dis}, 그냥 거리: {dis}')      
        
        wh_dis += max_dis #거리 합 구해
        # print("최소 거리: ", wh_dis)
    total = min(total, wh_dis) #합 중에 최소 구해
    # print("최소 거리 합: ", total)

print(total)