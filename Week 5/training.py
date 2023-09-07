def solution(n, lost, reserve):
    for r in reserve[:]:
        if r in lost:
            lost.remove(r)
            reserve.remove(r)
    
    have = n - len(lost)
    
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            continue
        
        if i+1 in reserve:
            have += 1
            reserve.remove(i+1)
            continue
        
        elif i-1 in reserve:
            have += 1
            reserve.remove(i-1)
            continue

            
    print(have)
    return have

n = 1
lost = [2]
reserve = [2]

solution(n, lost, reserve)