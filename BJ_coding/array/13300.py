import math
N, K = list(map(int, input().split())) #참가 학생 수, 최대 인원 수
w = [0] * 6
m = [0] * 6
room = 0

for _ in range(N):
    S, G = list(map(int, input().split()))
    if S == 0:
        w[G-1] += 1
    else:
        m[G-1] +=1

def ccount(arr, room):
    for i in arr:
        if i == 0:
            continue

        elif i > K:
            room += math.ceil(i/K)

        else:
            room += 1
    return room

room = ccount(w, room) + ccount(m, room)
print(room)