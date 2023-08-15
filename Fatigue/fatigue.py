from itertools import permutations

def solution(k, dungeons):
    answer = 0
    fatigue = k
    route = list(permutations(dungeons))
    
    for i in route:
        if answer == len(dungeons):
            break
        
        fatigue = k
        answer = 0
        
        for j in i:
            if fatigue >= j[0]:
                fatigue -= j[1] 
                answer += 1

    return answer