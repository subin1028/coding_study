import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while(1):
        min = heapq.heappop(scoville)
        if len(scoville) < 1 and min < K:
            return -1
        if min >= K:
            break
        min_2 = heapq.heappop(scoville)
        mix = min + (min_2 * 2)
        heapq.heappush(scoville, mix)
        answer += 1
        
    print(answer)
    return answer

# scoville = [1,2,3,9,10,12]
# k = 7

scoville = [0, 1]
k = 3

solution(scoville, k)