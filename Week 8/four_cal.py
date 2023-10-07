def solution(arr):
    answer = -1
    minmax = [0,0]
    
    # "-" 연산
    # 1. a-(b+c-d) // -뒤의 모든 식에 영향
    # 2. a-(b+c)-d // 두번째 -를 만나기 전까지의 식에만 영향
    # 3. a-(b)+c-d // -바로 뒤의 값에만 영향
    
    #"-"가 몇 번 나올지 모르기 때문에 최솟값, 최댓값을 모두 저장해두어야 함 
    sum_v = 0 # "-" 부호 만나기 전까지의 합
    # 최솟값 : min(-(sum + max), -sum + min)
    # 최댓값 : max(-(sum + min), (sum - 바로 전 값) - 바로 전 값 + max)
    
    #만약 1 - 3 + 5 - 8 이라면,
    for i in range(len(arr)-1, -1, -1): #리스트를 뒤에서부터 읽어오기
        if arr[i] == "+":
            continue
        elif arr[i] == "-":
            tmin, tmax = minmax
            minmax[0] = min(-(sum_v + tmax), -sum_v + tmin) #min(1번 연산, 2번 연산)
            minmax[1] = max(-(sum_v + tmin), (sum_v - int(arr[i+1]))-int(arr[i+1])+tmax)
            sum_v = 0
        else:
            sum_v += int(arr[i])
        
    answer = minmax[1] + sum_v    
    print(answer)        
    return answer

arr = ["1", "-", "3", "+", "5", "-", "8"]
solution(arr)

#처음부터 -의 개수를 알고 가는 건 어떤가