from collections import Counter
def solution(n, m, x, y, queries):
    answer = -1
    start = []
    
    for i in range(0, n):
        for j in range(0, m):
            start.append([i,j])
            
    for z in range(0, len(start)):
        i, j = start[z]
        for k, w in queries:
            if k == 0:
                j = max(0, j - w)
            elif k == 1:
                j = min(m-1, j + w)
            elif k == 2:
                i = max(0, i - w)
            elif k == 3:
                i == min(n-1, i + w)
        start[z] = [i,j]
        
        count = Counter(tuple(i) for i in start)
        answer = count[(0, 0)]

    return answer