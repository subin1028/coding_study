#맥주
from collections import deque

def bfs():
    queue = deque()
    queue.append([home[0], home[1]])
    while queue:
        x, y = queue.popleft()
        if abs(x-pen[0]) + abs(y-pen[1]) <= 1000: #20병 50m
            print("happy")
            return
        
        for i in range(num):
            if not visited[i]:
                nx, ny = cvs[i]
                if abs(x-nx) + abs(y-ny) <= 1000:
                    queue.append([nx, ny])
                    visited[i] = 1
    print("sad")
    return
    
test = int(input())
for _ in range(test):
    num = int(input())
    home = list(map(int, input().split()))
    cvs = [list(map(int, input().split())) for _ in range(num)]
    pen = list(map(int, input().split()))
    visited = [0 for _ in range(num+1)]
    bfs()