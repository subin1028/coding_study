def solution(routes):
    answer = 0
    routes.sort(key = lambda x: x[1])
    start = -30001    
    print(routes)
    
    for i in routes:
        if i[0] > start:
            answer += 1
            start = i[1]
    print(answer)
    return answer

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

solution(routes)