def solution(brown, yellow):
    total = brown + yellow
    divisor = []
    answer = [0,0]
    
    for i in range(1, total+1):
        if total % i == 0:
            divisor.append(i)
            
    for i in divisor:
        if ((i+2) * 2 + (yellow // i) * 2 == brown):
            answer[0] = i + 2
            answer[1] = yellow // i + 2
            break
        
    return answer