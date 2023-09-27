def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        mok = i // n
        na = i % n
        answer.append(max(mok, na)+1)
        
    return answer

n = 3
left = 2
right = 5
solution(n, left, right)