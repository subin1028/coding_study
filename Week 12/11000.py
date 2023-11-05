import heapq
N = int(input())
lecture = [list(map(int, input().split())) for _ in range(N)]

lecture.sort()
meeting = []
heapq.heappush(meeting, lecture[0][1])

for i in range(1, N):
    if meeting[0] > lecture[i][0]: #수업 이어서x
        heapq.heappush(meeting, lecture[i][1])
        
    else:
        heapq.heappop(meeting)
        heapq.heappush(meeting, lecture[i][1])

print(meeting)        
print(len(meeting))