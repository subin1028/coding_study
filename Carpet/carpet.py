def solution(brown, yellow):
    divisor = []
    answer = [0,0]
    
    for i in range(1, yellow+1):
        if yellow % i == 0:
            divisor.append(i)
            
    for i in divisor:
        if ((i+2) * 2 + (yellow // i) * 2 == brown):
            a = i + 2
            b = yellow // i + 2
            answer[0] = max(a,b)
            answer[1] = min(a,b)
         
    return answer