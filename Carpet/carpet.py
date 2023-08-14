def solution(brown, yellow):
    total = brown + yellow
    divisor = []
    answer = []
    for i in range(1, total+1):
        if total % i == 0:
            divisor.append(i)
    length = len(divisor)
            
    if length % 2 == 0:
        answer = [divisor[length//2], divisor[length//2 - 1]]
        
    else:
        answer = [divisor[length//2]] * 2
        
    return answer