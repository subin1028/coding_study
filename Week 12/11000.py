N = int(input())
lecture = [list(map(int, input().split())) for _ in range(N)]
time = [False for _ in range(N)]
cs = 0

#[[1, 3], [2, 4], [3, 5]]
lecture.sort()
for i in range(0, N-1):
    for j in range(i+1, N):
        if lecture[j][0] >= lecture[i][1] and time[j] == False:
            time[i] = True
            time[j] = True
            cs += 1 
            break
for t in time:
    if t == False:
        cs += 1
        
print(cs)
