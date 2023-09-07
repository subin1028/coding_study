def solution(n, lost, reserve):
    for r in reserve[:]:
        if r in lost:
            lost.remove(r)
            reserve.remove(r)
    lost.sort()
    
    for i in lost[:]:
        if i-1 in reserve: #1더한 값이 있을 경우
            reserve.remove(i-1)
            lost.remove(i)

        elif i+1 in reserve:
            reserve.remove(i+1)
            lost.remove(i)

    print(n-len(lost))
    return n - len(lost)

n = 5
lost = [2,4]
reserve = [1,3]

solution(n, lost, reserve)