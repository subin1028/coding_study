import sys

def check(now):
    for j in range(1, n):
        if abs(now[j] - now[j - 1]) > 1:   #차이가 1 초과인 경우 False
            return False
        if now[j] < now[j - 1]: #지나온 곳이 더 높을 때
            for k in range(l):  # l만큼 경사로 너비 필요 
                if j + k >= n or used[j + k] or now[j] != now[j + k]: # 범위 초과 or 이미 False or 설치할 곳 높이가 다름  
                    return False
                if now[j] == now[j + k]:  #높이가 같으면
                    used[j + k] = True #설치 처리
        elif now[j] > now[j - 1]: #현재 위치가 더 높을 때
            for k in range(l):
                if j - k - 1 < 0 or used[j - k - 1] or now[j - 1] != now[j - k - 1]:
                    return False
                if now[j - 1] == now[j - k - 1]:   # 높이가 같으면
                     used[j - k - 1] = True #설치 처리
    return True  #설치 완료 True 반환

n, l = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = 0

# 1. 가로 확인
for i in range(n):
    used = [False for _ in range(n)]  # 사용 여부
    if check(graph[i]):  # 한 행씩 넣어주기
        result += 1

# 2. 세로 확인
for i in range(n):
    used = [False for _ in range(n)]
    if check([graph[j][i] for j in range(n)]):  #한 열씩 넣어주기
        result += 1

print(result)