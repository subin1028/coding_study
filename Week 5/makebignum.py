def solution(number, k):
    answer = ''
    temp = []
    number = list(map(int, number))
    
    for i in number:
        if len(temp) == 0:
            temp.append(i)
            continue
            
        if k > 0:
            while temp[-1] < i:
                temp.pop()
                k -= 1
                
                if len(temp) == 0 or k <= 0:
                    break       
        temp.append(i)
    
    for j in temp[-(len(number) - k):]:
        answer += str(j)
        
    print(answer)
    return answer
    
number = "4177252841"
k = 4
ret= "775841"

solution(number, k)

