import heapq
def solution(operations):
    answer = []
    max2 = []
    for i in operations:
        if i[0] == "I":
            a = i.split(" ")[-1]
            heapq.heappush(answer, int(a))
        
        elif i == "D -1" and len(answer) > 0:
            if len(answer) == 0:
                break
            heapq.heappop(answer)
            
        elif i == "D 1" and len(answer) > 0:
            max2 = []
            if len(answer) == 0:
                break
            for i in answer:
                max2.append(-i)
            heapq.heapify(max2)
            rem = heapq.heappop(max2)
            answer.remove(-rem)
        
    if len(answer) == 0:
        answer = [0,0]
    else:
        r_max = max(answer)
        r_min = (heapq.heappop(answer))
        
        answer = [r_max, r_min]
        
    print(answer)
    return answer

operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
operations2 = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]

solution(operations2)