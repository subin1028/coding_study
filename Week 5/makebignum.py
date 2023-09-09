def solution(number, k):
    #if len([max(number):])가 len(number) - k보다 크면
    number = list(map(int, number))
    sort = list(set(number))
    sort.sort(reverse=True)
    idxs = [[] for i in range(len(sort))]
    start = k-1
    print(sort)
    answer = []

    for i in range(0, len(sort)):
        idx = [j for j, x in enumerate(number) if x == sort[i]]
        for m in range(0, len(idx)):
            idxs[i].append(idx[m]) 
    print(idxs)
    
    while(len(answer) < len(number) - k):
        for i in range(0, len(idxs)):
            for j in idxs[i]:
                if len(answer) > 0:
                    if j < start and j >= answer[-1][1]:
                        answer.append([i, j])
                        idxs[i].remove(j)
                        start += 1
                        print(answer)
                        break
                
                else:
                    if j < start:
                        answer.append([i, j])
                        idxs[i].remove(j)
                        start += 1
                        print(answer)
                        break
                  
                        
    print("answer : ", answer)
    return answer
    
number = "4177252841"
k = 4
ret= "775841"

solution(number, k)

