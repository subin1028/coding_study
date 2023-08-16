from itertools import permutations

def solution(k, dungeons):
    answer = 0
    fatigue = k
    times = []
    route = list(permutations(dungeons)) # 가능한 경로 생성
    
    for i in route:
        fatigue = k
        if answer == len(dungeons): #던전 개수와 횟수가 같을 경우
            break #종료
        
        answer = 0
        
        for j in i:
            if fatigue >= j[0]: 
                fatigue -= j[1] 
                answer += 1
                
            else:
                break
        times.append(answer)
        
    answer = max(times) #나온 결과 중 가장 큰 값 반환
    return answer