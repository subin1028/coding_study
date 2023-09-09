def solution(routes):
    answer = 1
    routes.sort()
    no = []
    
    
    for i in range(0, len(routes)-1):
        a, b = routes[1]
        for j in range(i+1, len(routes)):
            if routes[j][0] < b:
                a = max(a, routes[j][0])
                
                
            if routes[j][1] > a:
                b = min(b, routes[j][1])
                
            print(a,b)
                
    return answer

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

solution(routes)