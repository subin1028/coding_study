from collections import deque
N = int(input())
lecture = [list(map(int, input().split())) for _ in range(N)]
time = [False for _ in range(N)]
cs = 0
#[[1, 3], [2, 4], [3, 5]]
lecture.sort()
q = deque(lecture)
while q:
    _, t1 = q.popleft()
    for i in range(len(q)):
        t2, t3 = q.popleft()
    
        if t1 <= t2:
            cs += 1
            if len(q) == 1:
                cs += 1
                break
            continue
        
        else:
            q.append([t2, t3])
            print(len(q))
            if len(q) == 1:
                cs += 1
                break
print(cs)