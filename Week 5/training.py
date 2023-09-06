def solution(n, lost, reserve):
    answer = 0
    have = n - len(lost)
    
    for i in lost:
        for j in reserve:
            if abs(i - j) == 1:
                have += 1
                reserve.remove(j)
                break
                
            if i == j:
                break
    
    return have