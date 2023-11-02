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
if len(chicken) == M:
    for r,c in home:
        max_dis = N * 2 
        for cr, cc in chicken:
            dis = abs(r-cr) + abs(c-cc)
            max_dis = min(max_dis, dis)
            
        wh_dis += max_dis
        
else:
    total = N * 2 * M
    while combi_chicken:
        chickens = combi_chicken.popleft()
        for r,c in home:
            max_dis = N * 2 
            for cr, cc in chickens:
                dis = abs(r-cr) + abs(c-cc)
                max_dis = min(max_dis, dis)            
            
            wh_dis += max_dis
        total = min(total, wh_dis)
              
print(wh_dis)
print(total)